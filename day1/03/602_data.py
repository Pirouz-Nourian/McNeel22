import os
import compas
from compas.geometry import Point
from compas.geometry import NurbsCurve
from compas.geometry import Box
from compas.geometry import Frame

from compas_view2.app import App


points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)

box = Box(Frame.worldXY(), 0.8, 0.5, 0.3)

# =============================================================================
# Export
# =============================================================================

data = {"curve": curve, "box": box}

filepath = os.path.join(os.path.dirname(__file__), "session.json")

compas.json_dump(data, filepath)
