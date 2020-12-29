import sims4.commands

import careers
import services
import types

from sims.household import Household

from singletons import DEFAULT
from sims4.utils import flexmethod

@flexmethod
def get_hourly_pay(cls, inst, sim_info=DEFAULT, career_track=DEFAULT, career_level=DEFAULT, overmax_level=DEFAULT):
    inst_or_cls = inst if inst is not None else cls
    sim_info = sim_info if sim_info is not DEFAULT else inst.sim_info
    career_track = career_track if career_track is not DEFAULT else inst.current_track_tuning
    career_level = career_level if career_level is not DEFAULT else inst.level
    overmax_level = overmax_level if overmax_level is not DEFAULT else inst.overmax_level
    level_tuning = career_track.career_levels[career_level]
    hourly_pay = level_tuning.simoleons_per_hour
    if career_track.overmax is not None:
        hourly_pay += career_track.overmax.salary_increase * overmax_level
    hourly_pay = inst_or_cls._get_simolean_trait_bonus_pay(pay=hourly_pay, sim_info=sim_info, career_track=career_track, career_level=career_level)
    hourly_pay = int(hourly_pay)
    return int(round(hourly_pay / 4))

careers.career_base.CareerBase.get_hourly_pay = get_hourly_pay

def _update_cached_home_lot_value(self):
    home_zone = services.get_zone(self.home_zone_id)
    if not home_zone:
        return
    billable_value = 0
    billable_value += home_zone.lot.furnished_lot_value
    plex_service = services.get_plex_service()
    is_plex = plex_service.is_zone_a_plex(self.home_zone_id)
    for obj in services.object_manager().values():
        if obj.is_sim:
            continue
        if obj.get_household_owner_id() == self.id:
            continue
        if is_plex:
            if plex_service.get_plex_zone_at_position(obj.position, obj.level) != self.home_zone_id:
                continue
            else:
                if not home_zone.lot.is_position_on_lot(obj.position):
                    continue
            billable_value -= obj.current_value
            obj_inventory = obj.inventory_component
            if obj_inventory is not None:
                billable_value -= obj_inventory.inventory_value

    if billable_value < 0:
        logger.error('The billable household value for household {} is a negative number ({}). Defaulting to 0.', self, billable_value, owner='tastle')
        billable_value = 0
    self._cached_home_lot_value = billable_value

Household._update_cached_home_lot_value = types.MethodType(_update_cached_home_lot_value, Household)

@sims4.commands.Command('hellow', command_type=sims4.commands.CommandType.Live)
def _hellow(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("This is my first script mod")
