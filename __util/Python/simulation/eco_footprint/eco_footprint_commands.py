# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\eco_footprint\eco_footprint_commands.py
# Compiled at: 2020-05-06 21:52:03
# Size of source mod 2**32: 2659 bytes
import services
from eco_footprint.eco_footprint_enums import EcoFootprintStateType
from event_testing.test_events import TestEvent
from event_testing.game_option_tests import TestableGameOptions
from sims4.common import Pack
import sims4.commands

@sims4.commands.Command('eco_footprint.set_eco_footprint_enabled', pack=(Pack.EP09), command_type=(sims4.commands.CommandType.Live))
def set_eco_footprint_enabled(enabled: bool=True, _connection=None):
    street_service = services.street_service()
    if street_service is None:
        sims4.commands.automation_output('Pack not loaded', _connection)
        sims4.commands.cheat_output('Pack not loaded', _connection)
        return
    street_service.enable_eco_footprint = enabled
    services.get_event_manager().process_event((TestEvent.TestedGameOptionChanged), custom_keys=(
     TestableGameOptions.ECO_FOOTPRINT_GAMEPLAY,))
    return True


@sims4.commands.Command('eco_footprint.set_eco_footprint_value', pack=(Pack.EP09), command_type=(sims4.commands.CommandType.DebugOnly))
def set_eco_footprint_value(footprint_value: float, update_lot_footprint_values: bool=True, _connection=None):
    street_service = services.street_service()
    if street_service is None:
        sims4.commands.automation_output('Pack not loaded', _connection)
        sims4.commands.cheat_output('Pack not loaded', _connection)
        return
    street_provider = street_service.get_provider(services.current_street())
    street_provider.force_set_eco_footprint_value(footprint_value, update_lot_footprint_values)


@sims4.commands.Command('eco_footprint.set_eco_footprint_state', pack=(Pack.EP09), command_type=(sims4.commands.CommandType.Cheat))
def set_eco_footprint_state(state: EcoFootprintStateType, update_lot_footprint_values: bool=True, _connection=None):
    street_service = services.street_service()
    if street_service is None:
        sims4.commands.automation_output('Pack not loaded', _connection)
        sims4.commands.cheat_output('Pack not loaded', _connection)
        return
    street_provider = street_service.get_provider(services.current_street())
    street_provider.force_set_eco_footprint_state(state, update_lot_footprint_values)