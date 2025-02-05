from compas.geometry import Point
from compas.geometry import NurbsCurve
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Transformation
from compas.utilities import linspace
from compas.artists import Artist
import compas_rhino


points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)

frames = []
for t in linspace(curve.domain[0], curve.domain[1], 10):
    frames.append(curve.frame_at(t))

box = Box(Frame.worldXY(), 0.8, 0.5, 0.3)

boxes = []
for frame in frames:
    transformation = Transformation.from_frame_to_frame(box.frame, frame)
    boxes.append(box.transformed(transformation))

# =============================================================================
# Viz
# =============================================================================

artist = Artist(curve, layer="WS::Curve")
artist.clear_layer()
artist.draw()

compas_rhino.clear_layer("WS::frames")
for frame in frames:
    artist = Artist(frame, scale=0.5, layer="WS::frames")
    artist.draw()

compas_rhino.clear_layer("WS::boxes")

for box in boxes:
    artist = Artist(box, layer="WS::boxes")
    artist.draw()

## can also use the guids to delete the last drawn objects guids=artist.draw()
