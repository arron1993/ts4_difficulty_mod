# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\situations\situation_goal_proxy.py
# Compiled at: 2018-12-06 18:34:24
# Size of source mod 2**32: 1171 bytes
from situations.situation_goal import SituationGoal

class SituationGoalProxy(SituationGoal):
    REMOVE_INSTANCE_TUNABLES = ('_post_tests', )

    def on_goal_offered(self):
        super().on_goal_offered()
        if self._situation is None:
            return
        self._situation._on_proxy_situation_goal_added(self)

    def set_count(self, value):
        self._count = int(value)
        if self._count >= self._iterations:
            super()._on_goal_completed()
        else:
            self._on_iteration_completed()