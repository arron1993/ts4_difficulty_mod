# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\visualization\quad_tree_visualizer.py
# Compiled at: 2016-07-25 20:29:42
# Size of source mod 2**32: 2420 bytes
from _math import Vector2
from debugvis import Context, KEEP_ALTITUDE
from sims4.color import Color
from sims4.geometry import Polygon, ObjectQuadTreeQueryFlag, QtCircle
import placement, routing, services, sims4.math, terrain

class QuadTreeVisualizer:

    def __init__(self, layer):
        self.layer = layer
        self._start()

    def _start(self):
        services.current_zone().on_quadtree_changed_for_debug_viz.append(self._on_quadtree_changed)
        self._on_quadtree_changed()

    def stop(self):
        services.current_zone().on_quadtree_changed_for_debug_viz.remove(self._on_quadtree_changed)

    def _on_quadtree_changed(self):
        quadtree = services.sim_quadtree()
        if quadtree is None:
            return
        bounds = QtCircle(Vector2(0, 0), 10000)
        with Context(self.layer) as (layer):
            filter_visualizers = ((placement.ItemType.SIM_POSITION, Color.GREEN),
             (
              placement.ItemType.SIM_INTENDED_POSITION, Color.YELLOW),
             (
              placement.ItemType.ROUTE_GOAL_SUPPRESSOR, Color.RED),
             (
              placement.ItemType.ROUTABLE_OBJECT_SURFACE, Color.CYAN))
            for quadtree_filter, color in filter_visualizers:
                layer.set_color(color)
                for o in quadtree.query(bounds=bounds, surface_id=(routing.SurfaceIdentifier(0, 0, 0)), filter=quadtree_filter, flags=(ObjectQuadTreeQueryFlag.IGNORE_SURFACE)):
                    if isinstance(o[2], Polygon):
                        layer.add_polygon((o[2]), altitude=0.1, routing_surface=(o[3]))
                    else:
                        height = terrain.get_lot_level_height(o[2].center.x, o[2].center.y, o[3].secondary_id, services.current_zone_id()) + 0.1
                        layer.add_circle((sims4.math.Vector3(o[2].center.x, height, o[2].center.y)), (o[2].radius), altitude=KEEP_ALTITUDE)