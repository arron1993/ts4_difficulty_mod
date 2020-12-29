import os

import sims4.commands

import careers
import services
import types

from sims.household import Household

from singletons import DEFAULT
from sims4.utils import flexmethod
from sims4.log import Logger

def log(text):
    path = os.path.join("C:", "Users", "moorey", "projects", "ts4_difficulty_mod", "src", "log.txt")
    with open(path, 'a') as f:
        f.write(f"{text}\n")

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
    return int(round(hourly_pay * 0.33))

careers.career_base.CareerBase.get_hourly_pay = get_hourly_pay

import objects

@property
def price(self):
    log("Price")
    return round(int(self._catalog_price * 1.5))

# objects.definition.Definition.price = price

from sims.bills import Bills
def _get_property_taxes(self):
    log("Get property taxes")
    plex_service = services.get_plex_service()
    if plex_service.is_zone_an_apartment((self._household.home_zone_id), consider_penthouse_an_apartment=False):
        return 0
    billable_household_value = self._household.household_net_worth(billable=True)
    tax_value = 0
    for bracket in Bills.BILL_BRACKETS:
        lower_bound = bracket.value_range.lower_bound
        if billable_household_value >= lower_bound:
            upper_bound = bracket.value_range.upper_bound
            if upper_bound is None:
                upper_bound = billable_household_value
            bound_difference = upper_bound - lower_bound
            value_difference = billable_household_value - lower_bound
            if value_difference > bound_difference:
                value_difference = bound_difference
            value_difference *= 0.33
            tax_value += value_difference
    return tax_value

Bills._get_property_taxes = _get_property_taxes
@sims4.commands.Command('hellow', command_type=sims4.commands.CommandType.Live)
def _hellow(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("This is my first script mod")
