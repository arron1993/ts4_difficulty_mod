# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\narrative\narrative_environment_support.py
# Compiled at: 2018-10-30 02:32:06
# Size of source mod 2**32: 2634 bytes
from event_testing.test_variants import RegionTest
from narrative.narrative_enums import NarrativeEnvironmentParams
from sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, OptionalTunable, TunableMapping, TunableEnumEntry, TunableTuple, TunableSimMinute, Tunable
from weather.weather_loot_ops import WeatherSetOverrideForecastLootOp

class NarrativeEnvironmentOverride(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'supported_regions':OptionalTunable(description='\n            If set, this override is only applicable in the specified regions.\n            ',
       tunable=RegionTest.TunableFactory(locked_args={'tooltip':None,  'subject':None})), 
     'weather_forecast_override':WeatherSetOverrideForecastLootOp.TunableFactory(description="\n            If Seasons pack is installed, this forecast is used to override \n            the affected region's weather.\n            "), 
     'narrative_environment_params':TunableMapping(description='\n            The various parameters to set when the narrative is enabled.\n            ',
       key_type=TunableEnumEntry(description='\n                The parameter that we wish to change.\n                ',
       tunable_type=NarrativeEnvironmentParams,
       default=None),
       value_type=TunableTuple(interpolation_time=TunableSimMinute(description='\n                    The time over which to transition to the new value,\n                    if this occurs during simulation.\n                    ',
       minimum=0.0,
       default=15.0),
       value=Tunable(description='\n                    The value that we will set this parameter to.\n                    ',
       tunable_type=float,
       default=1.0)))}

    def should_apply(self):
        if self.supported_regions is not None:
            return self.supported_regions()
        return True