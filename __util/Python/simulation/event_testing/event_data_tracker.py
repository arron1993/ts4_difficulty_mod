# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\event_testing\event_data_tracker.py
# Compiled at: 2020-08-05 01:08:11
# Size of source mod 2**32: 30191 bytes
import itertools, alarms, services, sims4.log
from collections import namedtuple, Counter
from date_and_time import TimeSpan, DateAndTime
from distributor.rollback import ProtocolBufferRollback
from event_testing.event_data_const import TimeData
from event_testing.event_data_object import EventDataObject
from event_testing.objective_completion_type import ObjectiveCompletionType
from event_testing.resolver import DataResolver
from event_testing.results import TestResultNumeric
from gsi_handlers.achievement_handlers import archiver
logger = sims4.log.Logger('EventDataTracker')
ObjectiveUpdateInfo = namedtuple('ObjectiveUpdateInfo', ['current_value', 'objective_value', 'is_money', 'from_init', 'show_progress'])

class EventDataTracker:
    TIME_DATA_UPDATE_RATE = 60000

    def __init__(self):
        self._completed_milestones = set()
        self._completed_objectives = set()
        self._reset_objectives = set()
        self._sent_milestones = set()
        self._sent_objectives = set()
        self._data_object = EventDataObject()
        self._tracker_dirty = False
        self._dirty_objective_state = {}
        self._last_objective_state = {}
        self._unlocked_hidden_aspiration_tracks = set()
        self._sent_unlocked_hidden_aspiration_tracks = set()
        self._total_milestone_completion_count = Counter()
        self.update_alarm_handle = None
        self.sim_time_on_connect = DateAndTime(0)
        self.server_time_on_connect = DateAndTime(0)
        self.sim_time_last_update = DateAndTime(0)
        self.server_time_last_update = DateAndTime(0)
        self.latest_objective = None
        self._event_trackers = {}

    @property
    def data_object(self):
        return self._data_object

    @property
    def owner_sim_info(self):
        raise NotImplementedError

    @property
    def simless(self):
        return False

    def _get_milestone_manager(self):
        raise NotImplementedError

    def get_objective_count(self, objective):
        return self._data_object.get_objective_count(objective)

    def get_objectives(self, milestone):
        return tuple(itertools.chain(milestone.objectives, self.get_additional_objectives(milestone)))

    def get_additional_objectives(self, milestone):
        return []

    def _should_handle_event(self, milestone, event, resolver: DataResolver):
        return not resolver.sim_info.is_npc

    def _should_test_objective(self, milestone, objective):
        return True

    def tracker_complete(self, milestone, objective):
        self.complete_objective(objective, milestone)
        goal_value = objective.goal_value()
        self.update_objective(objective, goal_value, goal_value, objective.is_goal_value_money, objective.show_progress)
        completed_milestone = False
        if not self.milestone_completed(milestone):
            objectives_completed = sum((1 for objective_to_complete in self.get_objectives(milestone) if self.objective_completed(objective_to_complete)))
            if objectives_completed >= self.required_completion_count(milestone):
                self.complete_milestone(milestone, self.owner_sim_info)
                completed_milestone = True
        else:
            self.send_if_dirty()
            if completed_milestone:
                self.post_completion_ui_update(milestone, self.owner_sim_info)
            else:
                self.remove_event_tracker(objective)

    def add_event_tracker(self, objective, event_tracker):
        if event_tracker.setup():
            self._event_trackers[objective] = event_tracker
        else:
            event_tracker.clear()

    def remove_event_tracker(self, objective):
        self._event_trackers[objective].clear()
        del self._event_trackers[objective]

    def handle_event(self, milestone, event, resolver, debug_objectives_to_force_complete=None):
        if resolver.on_zone_load:
            if not milestone.should_test_on_zone_load():
                return
            else:
                return self._should_handle_event(milestone, event, resolver) or None
            log_enabled = archiver.enabled and not resolver.on_zone_load
            if log_enabled:
                milestone_event = self.gsi_event(event)
                milestone_process_data = []
        else:
            milestone_was_completed = False
            if not self.milestone_completed(milestone):
                objectives_completed = 0
                objectives = self.get_objectives(milestone)
                if not objectives:
                    if not milestone.can_complete_without_objectives:
                        return
                for objective in objectives:
                    milestone_event_data = None
                    if self.objective_completed(objective):
                        objectives_completed += 1
                        continue
                    if not self._should_test_objective(milestone, objective):
                        continue
                    if log_enabled:
                        milestone_event_data = self.gsi_event_data(milestone, objective, True, 'Objective Completed')
                    if debug_objectives_to_force_complete:
                        if objective in debug_objectives_to_force_complete:
                            test_result = objective.increment_data(resolver, self)
                        else:
                            test_result = objective.run_test(event, resolver, self)
                        if test_result:
                            completion_type = self.complete_objective(objective, milestone)
                            milestone_was_completed = completion_type == ObjectiveCompletionType.MILESTONE_COMPLETE
                            objectives_completed += 1
                            goal_value = objective.goal_value()
                            self.update_objective(objective, goal_value, goal_value, objective.is_goal_value_money, objective.show_progress)
                        else:
                            if log_enabled:
                                milestone_event_data['test_result'] = test_result.reason
                                milestone_event_data['completed'] = False
                                milestone_process_data.append(milestone_event_data)
                            if isinstance(test_result, TestResultNumeric):
                                self.update_objective(objective, test_result.current_value, test_result.goal_value, test_result.is_money, objective.show_progress)

                if objectives_completed >= self.required_completion_count(milestone) or milestone_was_completed:
                    self.complete_milestone(milestone, resolver.sim_info)
                    milestone_was_completed = True
        if log_enabled:
            milestone_event['Objectives Processed'] = milestone_process_data
            self.post_to_gsi(milestone_event)
        self.send_if_dirty()
        if milestone_was_completed:
            self.post_completion_ui_update(milestone, resolver.sim_info)

    def gsi_event(self, event):
        return {'event': str(event)}

    def gsi_event_data(self, milestone, objective, completed, result):
        return {'milestone':milestone.__name__, 
         'completed':completed,  'test_type':objective.objective_test.__class__.__name__, 
         'test_result':result}

    def post_to_gsi(self, message):
        pass

    def send_if_dirty(self):
        if self._dirty_objective_state:
            self._send_objectives_update_to_client()
            self._dirty_objective_state = {}
        if self._tracker_dirty:
            self._send_tracker_to_client()
            self._tracker_dirty = False

    def _update_objectives_msg_for_client(self, msg):
        message_loaded = False
        for objective, value in list(self._dirty_objective_state.items()):
            if value.from_init or objective not in self._last_objective_state or self._last_objective_state[objective] != value.current_value:
                msg.goals_updated.append(int(objective.guid64))
                msg.goal_values.append(int(value[0]))
                msg.goal_objectives.append(int(value[1]))
                msg.goals_that_are_money.append(bool(value[2]))
                msg.goals_that_show_progress.append(bool(value[4]))
                self._last_objective_state[objective] = value[0]
                message_loaded = True

        return message_loaded

    def clear_objective_updates_cache(self, milestone):
        for objective in self.get_objectives(milestone):
            if objective.guid64 in self._last_objective_state:
                del self._last_objective_state[objective.guid64]

    def _send_tracker_to_client(self, init=False):
        raise NotImplementedError

    def _send_objectives_update_to_client(self):
        raise NotImplementedError

    def required_completion_count(self, milestone):
        return milestone.objective_completion_count() or len(self.get_objectives(milestone))

    def update_objective(self, objective, current_value, objective_value, is_money, show_progress, from_init=False):
        self._dirty_objective_state[objective] = ObjectiveUpdateInfo(current_value, objective_value, is_money, from_init, show_progress)

    def complete_milestone(self, milestone, sim_info):
        self._completed_milestones.add(milestone)
        if milestone.track_completion_count:
            self._total_milestone_completion_count[milestone.guid64] += 1
        self._tracker_dirty = True

    def post_completion_ui_update(self, milestone, sim_info):
        pass

    def milestone_completed(self, milestone):
        return milestone in self._completed_milestones

    def milestone_sent(self, milestone):
        return milestone in self._sent_milestones

    def get_milestone_completion_count(self, milestone):
        if milestone.track_completion_count:
            return self._total_milestone_completion_count.get(milestone.guid64, 0)

    def reset_milestone(self, milestone):
        if milestone in self._completed_milestones:
            self._completed_milestones.remove(milestone)
        if milestone in self._sent_milestones:
            self._sent_milestones.remove(milestone)

    def complete_objective(self, objective_instance, milestone):
        self.latest_objective = objective_instance
        if objective_instance in self._reset_objectives:
            self._reset_objectives.remove(objective_instance)
        if objective_instance in self._sent_objectives:
            self._sent_objectives.remove(objective_instance)
        self._completed_objectives.add(objective_instance)
        self._tracker_dirty = True
        return ObjectiveCompletionType.OBJECTIVE_COMPLETE

    def objective_completed(self, objective_instance):
        return objective_instance in self._completed_objectives

    def objective_sent(self, objective_instance):
        return objective_instance in self._sent_objectives

    def reset_objective(self, objective_instance):
        if objective_instance in self._completed_objectives:
            self._completed_objectives.remove(objective_instance)
        if objective_instance in self._sent_objectives:
            self._sent_objectives.remove(objective_instance)
        self._reset_objectives.add(objective_instance)
        self._tracker_dirty = True

    def unlocked_hidden_aspiration_track_sent(self, unlocked_hidden_aspiration_track):
        return unlocked_hidden_aspiration_track in self._sent_unlocked_hidden_aspiration_tracks

    def update_timers(self):
        server_time_add = self.server_time_since_update()
        sim_time_add = self.sim_time_since_update()
        self._data_object.add_time_data(TimeData.SimTime, sim_time_add)
        self._data_object.add_time_data(TimeData.ServerTime, server_time_add)

    def set_update_alarm(self):
        if self.update_alarm_handle is not None:
            return
        self.sim_time_on_connect = services.time_service().sim_now
        self.server_time_on_connect = services.server_clock_service().now()
        self.sim_time_last_update = self.sim_time_on_connect
        self.server_time_last_update = self.server_time_on_connect
        self.update_alarm_handle = alarms.add_alarm(self, TimeSpan(self.TIME_DATA_UPDATE_RATE), self._update_timer_alarm, True)

    def clear_tracked_client_data(self):
        self._reset_objectives.clear()
        self._sent_milestones.clear()
        self._sent_objectives.clear()
        self._tracker_dirty = False
        self._dirty_objective_state.clear()
        self._last_objective_state.clear()
        self._sent_unlocked_hidden_aspiration_tracks.clear()

    def clear_update_alarm(self):
        if self.update_alarm_handle is not None:
            alarms.cancel_alarm(self.update_alarm_handle)
            self.update_alarm_handle = None
            self.update_timers()

    def _update_timer_alarm(self, _):
        raise NotImplementedError('Must override in subclass')

    def server_time_since_update(self):
        time_delta = services.server_clock_service().now() - self.server_time_last_update
        self.server_time_last_update = services.server_clock_service().now()
        return time_delta.in_ticks()

    def sim_time_since_update(self):
        time_delta = services.time_service().sim_now - self.sim_time_last_update
        self.sim_time_last_update = services.time_service().sim_now
        return time_delta.in_ticks()

    def save(self, blob=None):
        if blob is not None:
            self._data_object.save(blob)
            milestones_completed = set(blob.milestones_completed) | {milestone.guid64 for milestone in self._completed_milestones}
            objectives_completed = set(blob.objectives_completed) | {objective.guid64 for objective in self._completed_objectives}
            blob.ClearField('milestones_completed')
            blob.ClearField('objectives_completed')
            blob.ClearField('milestone_completion_counts')
            blob.milestones_completed.extend(milestones_completed)
            blob.objectives_completed.extend(objectives_completed)
            for milestone_guid, completion_count in self._total_milestone_completion_count.items():
                with ProtocolBufferRollback(blob.milestone_completion_counts) as (count_data):
                    count_data.milestone_guid = milestone_guid
                    count_data.completion_count = completion_count

    def load(self, blob=None):
        milestone_manager = self._get_milestone_manager()
        objective_manager = services.get_instance_manager(sims4.resources.Types.OBJECTIVE)
        if blob is not None:
            for milestone_id in blob.milestones_completed:
                milestone = milestone_manager.get(milestone_id)
                if milestone is not None:
                    self._completed_milestones.add(milestone)

            for objective_id in blob.objectives_completed:
                objective = objective_manager.get(objective_id)
                if objective is not None:
                    self._completed_objectives.add(objective)

            for count_data in blob.milestone_completion_counts:
                milestone = milestone_manager.get(count_data.milestone_guid)
                if milestone is not None and milestone.track_completion_count:
                    self._total_milestone_completion_count[count_data.milestone_guid] = count_data.completion_count

            self._data_object.load(blob)
        for objective_id, objective_data in self._data_object.get_objective_count_data().items():
            if objective_manager.get(objective_id) is None:
                logger.info('Trying to load unavailable OBJECTIVE resource: {}', objective_id)
                continue
            objective = objective_manager.get(objective_id)
            objective_count = objective_data.get_count()
            objective_value = objective.goal_value()
            if objective_count >= objective_value:
                self._completed_objectives.add(objective)

    def send_event_data_to_client(self):
        if not self.simless:
            owner_sim_info = self.owner_sim_info
            if not owner_sim_info is None:
                if owner_sim_info.is_npc:
                    return
        objective_manager = services.get_instance_manager(sims4.resources.Types.OBJECTIVE)
        objectives_in_progress = set()
        for objective_id, objective_data in self._data_object.get_objective_count_data().items():
            if objective_manager.get(objective_id) is None:
                logger.info('Trying to load unavailable OBJECTIVE resource: {}', objective_id)
                continue
            objective = objective_manager.get(objective_id)
            objective_count = objective_data.get_count()
            objective_value = objective.goal_value()
            self.update_objective(objective, objective_count, objective_value, objective.is_goal_value_money, objective.show_progress)
            objectives_in_progress.add(objective_id)

        for objective in objective_manager.types.values():
            if objective.guid64 not in objectives_in_progress:
                self.update_objective(objective, 0, objective.goal_value(), objective.is_goal_value_money, objective.show_progress)

        self._send_objectives_update_to_client()
        self._send_tracker_to_client(init=True)

    def refresh_progress(self, sim_info=None):
        if sim_info is None:
            sim_info = self.owner_sim_info
        services.get_event_manager().process_test_events_for_objective_updates(sim_info)
        self._send_objectives_update_to_client()
        self._send_tracker_to_client(init=True)

    def reset_data(self):
        self._completed_milestones = set()
        self._completed_objectives = set()
        self._reset_objectives = set()
        self._sent_milestones = set()
        self._sent_objectives = set()
        self._data_object = EventDataObject()
        self._tracker_dirty = False
        self._dirty_objective_state = {}
        self._last_objective_state = {}
        self.sim_time_on_connect = DateAndTime(0)
        self.server_time_on_connect = DateAndTime(0)
        self.sim_time_last_update = DateAndTime(0)
        self.server_time_last_update = DateAndTime(0)
        self.latest_objective = None
        for event_tracker in self._event_trackers.values():
            event_tracker.clear()

        self._event_trackers.clear()

    def get_last_updated_value_for_objective(self, objective_id):
        return self._last_objective_state.get(objective_id)