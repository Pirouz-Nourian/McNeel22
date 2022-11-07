from compas.geometry import Point
from compas.geometry import NurbsCurve
from compas_view2.app import App


points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)

print(curve)

viewer=App()
viewer.add(curve.to_polyline())# the viewer in future will be able to directly view a curve as the BReps are already supported.
viewer.show()