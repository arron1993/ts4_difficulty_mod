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
    log("get_hourly_pay called")
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
    log("price called")
    return 250

objects.definition.Definition.price = price

@sims4.commands.Command('hellow', command_type=sims4.commands.CommandType.Live)
def _hellow(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("This is my first script mod")
