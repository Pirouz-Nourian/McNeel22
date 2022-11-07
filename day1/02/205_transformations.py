from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation
from compas.geometry import Rotation
from compas_view2.app import App
from math import radians

# create a box in the world coordinate system
box1 = Box(frame=Frame.worldXY(), xsize=1, ysize=2, zsize=2)

# define a new location for the box
location = Point(0.5, 0.5, 0.5)

# compute a translation transformation
vector = location - box1.frame.point
translation = Translation.from_vector(vector)
rotation= Rotation.from_axis_and_angle([1,0,0],radians(90))

# generae a transformed copy of the box
box2 = box1.transformed(translation)
box3=box2.transformed(rotation)
# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [3, -5, 3]
viewer.view.camera.look_at([0, 0, 0])

viewer.add(box1, show_faces=False)
viewer.add(box1.frame, linewidth=3)

viewer.add(box2, show_faces=False)
viewer.add(box2.frame, linewidth=3)

viewer.show()
