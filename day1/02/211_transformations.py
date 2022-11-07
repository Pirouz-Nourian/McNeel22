from compas.geometry import Box
from compas.geometry import Frame
from compas_view2.app import App

import random
from compas.geometry import Pointcloud
from compas.geometry import Transformation
#for viewing many objects use collections!
from compas_view2.objects import Collection
from compas.colors import Color

# create a pointcloud
# assign a coordinate frame to every point in the cloud
# reposition a transformed copy of the box in each coordinate system
# use random colors for visualisation


box = Box(frame=Frame.worldXY(), xsize=0.3, ysize=0.2, zsize=0.1)

cloud=Pointcloud.from_bounds(8,5,3,53)
frames=[]
boxes = []
for point in cloud:
    xaxis = random.random(), random.random(), random.random()
    yaxis = random.random(), random.random(), random.random()

    frame = Frame(point, xaxis, yaxis)

    X = Transformation.from_frame_to_frame(box.frame, frame)

    boxes.append(box.transformed(X))


# =============================================================================
# Viz
# =============================================================================

# viewer = App()

# viewer.add(box)
# viewer.add(cloud)
# # for frame in frames:
# #     color=Color.from_i(random.random())#an idiosyncratic remnant of the early versions of compas
    
# #     viewer.add(box, facecolor=color)
# #     viewer.add(frame)


# viewer.add (Collection(boxes, [{"facecolor": Color.from_i(random.ranom())} for _ in boxes]))
# # alternatively:
# # viewer.add(Collection(frames))
# # viewer.add(Collection(boxes))

# viewer.show()

viewer = App()

viewer.add(box)
viewer.add(cloud)
properties=[{"facecolor": Color.from_i(random.random())} for _ in boxes]
viewer.add(Collection(boxes,properties))

viewer.show()
