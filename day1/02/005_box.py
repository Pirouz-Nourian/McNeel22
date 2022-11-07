from compas.geometry import Box
from compas.geometry import Frame

# define a coordinate system
frame = Frame.worldXY()

# define a box in the coordinate system
box = Box(frame=frame, xsize=1, ysize=1, zsize=1)

print(box.frame)
print(box.xsize)
print(box.ysize)
print(box.zsize)
