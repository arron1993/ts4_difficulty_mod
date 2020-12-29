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
    return self._catalog_price * 1.5

objects.definition.Definition.price = price

from sims4.tuning.tunable import TunableList, TunableTuple, TunablePercent, TunableInterval
import sims
BILL_BRACKETS = TunableList(description="\n        A list of brackets that determine the percentages that each portion of\n        a household's value is taxed at.\n        \n        ex: The first $2000 of a household's value is taxed at 10%, and\n        everything after that is taxed at 15%.\n        ",
    tunable=TunableTuple(description='\n            A value range and tax percentage that define a bill bracket.\n            ',
    value_range=TunableInterval(description="\n                A tunable range of integers that specifies a portion of a\n                household's total value.\n                ",
    tunable_type=int,
    default_lower=0,
    default_upper=None),
    tax_percentage=TunablePercent(description="\n                A tunable percentage value that defines what percent of a\n                household's value within this value_range the player is billed\n                for.\n                ",
    default=33)))

sims.bills.Bills.BILL_BRACKETS = BILL_BRACKETS

@sims4.commands.Command('hellow', command_type=sims4.commands.CommandType.Live)
def _hellow(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("This is my first script mod")
