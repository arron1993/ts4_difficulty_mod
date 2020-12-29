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

import sims4

def load_object(self, object_data, **kwargs):
    log(f"Load Object {object_data.cost}")
    if object_data.HasField('owner_id'):
        self._household_owner_id = object_data.owner_id
    else:
        if self.is_downloaded:
            self.base_value = self.catalog_value * 1.5
        else:
            self.base_value = object_data.cost * 1.5
        self.new_in_inventory = object_data.is_new
        (super().load_object)(object_data, **kwargs)
        if object_data.HasField('texture_id'):
            if self.canvas_component is not None:
                self.canvas_component.set_painting_texture_id(object_data.texture_id)
        if object_data.HasField('needs_depreciation'):
            self._needs_depreciation = object_data.needs_depreciation
        if object_data.HasField('needs_post_bb_fixup'):
            self._needs_post_bb_fixup = object_data.needs_post_bb_fixup
        else:
            self._needs_post_bb_fixup = self._needs_depreciation
    inventory = self.inventory_component
    if inventory is not None:
        inventory.load_items(object_data.unique_inventory)
    if sims4.protocol_buffer_utils.has_field(object_data, 'buildbuy_use_flags'):
        self._build_buy_use_flags = object_data.buildbuy_use_flags
    self.is_new_object = object_data.is_new_object
    if self.is_new_object:
        self.add_dynamic_component(objects.components.types.NEW_OBJECT_COMPONENT)
    if object_data.persisted_tags is not None:
        self.append_tags(set(object_data.persisted_tags))

objects.game_object.GameObject.load_object = load_object

@sims4.commands.Command('hellow', command_type=sims4.commands.CommandType.Live)
def _hellow(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("This is my first script mod")
