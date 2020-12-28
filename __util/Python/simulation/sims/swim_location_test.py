# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\sims\swim_location_test.py
# Compiled at: 2019-07-11 19:51:11
# Size of source mod 2**32: 4200 bytes
from event_testing import test_base
from event_testing.results import TestResult
from event_testing.test_events import cached_test
from interactions import ParticipantTypeSingle
from routing import SurfaceType
from sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableEnumEntry, TunableVariant, Tunable

class _SwimInPoolTest:

    def evaluate(self, sim, in_tooltip, invert):
        if sim.routing_surface.type == SurfaceType.SURFACETYPE_POOL:
            if sim.in_pool:
                if invert:
                    return TestResult(False, 'Test inverted: {} is in a pool.', sim, tooltip=in_tooltip)
                return TestResult.TRUE
        if invert:
            return TestResult.TRUE
        return TestResult(False, '{} is not in a pool.', sim, tooltip=in_tooltip)


class _SwimInOceanTest:

    def evaluate(self, sim, in_tooltip, invert):
        if sim.routing_surface.type == SurfaceType.SURFACETYPE_POOL:
            if not sim.in_pool:
                if invert:
                    return TestResult(False, 'Test inverted: {} is in an ocean.', sim, tooltip=in_tooltip)
                return TestResult.TRUE
        if invert:
            return TestResult.TRUE
        return TestResult(False, '{} is not in an ocean.', sim, tooltip=in_tooltip)


class _SimInWaterTest:

    def evaluate(self, sim, in_tooltip, invert):
        if sim.routing_surface.type == SurfaceType.SURFACETYPE_POOL:
            if invert:
                return TestResult(False, 'Test inverted: {} is in the water.', sim, tooltip=in_tooltip)
            return TestResult.TRUE
        if invert:
            return TestResult.TRUE
        return TestResult(False, '{} is not in the water.', sim, tooltip=in_tooltip)


class SwimLocationTest(HasTunableSingletonFactory, AutoFactoryInit, test_base.BaseTest):
    FACTORY_TUNABLES = {'subject':TunableEnumEntry(description='\n            The subject to test to determine whether they are\n            in a certain body of water\n            ',
       tunable_type=ParticipantTypeSingle,
       default=ParticipantTypeSingle.Actor), 
     'test':TunableVariant(description='\n            The type of body of water we are testing for\n            ',
       default='swim_in_pool',
       locked_args={'swim_in_pool':_SwimInPoolTest(), 
      'swim_in_ocean':_SwimInOceanTest(), 
      'any':_SimInWaterTest()}), 
     'invert':Tunable(description='\n            Inverts the result of tuned test.\n            ',
       tunable_type=bool,
       default=False)}

    def get_expected_args(self):
        return {'subjects': self.subject}

    @cached_test
    def __call__(self, subjects):
        subject = next(iter(subjects), None)
        if subject is None:
            return TestResult(False, 'SwimLocationTest: Subject is None')
            if subject.is_sim:
                sim = subject.get_sim_instance()
                if sim is None:
                    return TestResult(False, 'SwimLocationTest: Sim is not instanced')
                return self.test.evaluate(sim, self.tooltip, self.invert)
        else:
            return TestResult(False, 'SwimLocationTest: Subject is not a Sim')