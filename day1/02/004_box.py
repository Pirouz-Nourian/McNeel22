from compas.geometry import Box
from compas.geometry import Frame


# define a coordinate system
frame = Frame.worldXY()

# create a box in the coordinate system
box = Box(frame=frame, xsize=1, ysize=1, zsize=1)


print(box)
print(box.xsize)
print(box.edges)
print(box.faces)
print(type(box))
from compas_view2.app import App
