from compas.geometry import Point
from compas.geometry import NurbsCurve
from compas.geometry import Surface
from compas.geometry import Plane
from compas.geometry import Frame
from compas.geometry import Box
from compas.utilities import linspace
from compas.artists import Artist

# =============================================================================
# Curve
# =============================================================================

points = [
    Point(0, 0, 0),
    Point(2, 2, 0),
    Point(4, -4, 0),
    Point(6, 0, 0),
]

curve = NurbsCurve.from_points(points)

# =============================================================================
# Params
# =============================================================================

N = 11
W = 0.4
H = 0.2

# =============================================================================
# Offsets
# =============================================================================

outer = curve.copy()
outer.offset(0.5 * W, [0, 0, -1])

inner = curve.copy()
inner.offset(0.5 * W, [0, 0, +1])

# =============================================================================
# Frames
# =============================================================================

params_0 = list(linspace(curve.domain[0], curve.domain[1], N))
frames_0 = [curve.frame_at(t) for t in params_0]

# =============================================================================
# 1st Course
# =============================================================================

opoints_0 = []
ipoints_0 = []
boxes=[]
for frame in frames_0:
    plane = Plane(frame.point, frame.xaxis)
    bbox = Box(Frame(frame.point, frame.yaxis, frame.zaxis), 1, 1, 0.1)
    boxes.append(bbox)
    surface = Surface.from_plane(plane, bbox)

    points = surface.intersections_with_curve(outer)
    opoints_0.append(points[0])

    points = surface.intersections_with_curve(inner)
    ipoints_0.append(points[0])

# =============================================================================
# Viz
# =============================================================================

Artist.clear()

Artist(curve).draw()
Artist(outer).draw()
Artist(inner).draw()

for frame in frames_0:
    Artist(frame, scale=0.3).draw()

for point in opoints_0:
    Artist(point).draw()

for point in ipoints_0:
    Artist(point).draw()

for box in boxes:
    Artist(box).draw()
