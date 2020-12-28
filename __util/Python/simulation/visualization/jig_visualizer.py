# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\visualization\jig_visualizer.py
# Compiled at: 2017-03-10 20:27:23
# Size of source mod 2**32: 1792 bytes
import sims4.math
from debugvis import Context
from sims4.color import pseudo_random_color
from socials.jigs import jig_utils
DEFAULT_ALTITUDE_CHANGE = 0.05
DEFAULT_ALTITUDE_CHANGE_VECTOR = sims4.math.Vector3(0, DEFAULT_ALTITUDE_CHANGE, 0)

class JigVisualizer:

    def __init__(self, layer):
        self.layer = layer
        self._start()

    def _start(self):
        jig_utils.on_jig_changed.append(self._on_jig_changed)

    def stop(self):
        jig_utils.on_jig_changed.remove(self._on_jig_changed)

    def _on_jig_changed(self, sim_a_transform=None, sim_b_transform=None, polygon=None, preserve=True):
        with Context((self.layer), preserve=preserve) as (layer):
            if preserve:
                self.draw_jig(layer, sim_a_transform, sim_b_transform, polygon)

    @staticmethod
    def draw_jig(layer, sim_a_transform, sim_b_transform, polygon):
        color = pseudo_random_color(id(polygon))
        layer.add_point((sim_a_transform.translation), color=color)
        layer.add_arrow_for_transform(sim_a_transform, color=color)
        layer.add_arrow_for_transform(sim_b_transform, color=color)
        layer.add_polygon(polygon, color=color)