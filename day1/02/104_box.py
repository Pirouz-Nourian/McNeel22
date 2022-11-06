from compas.geometry import Box
from compas.geometry import Frame

from compas_view2.app import App

box = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

viewer = App()
viewer.view.camera.position = [1, -2, 2]
viewer.view.camera.target = [0, 0, 0]

viewer.add(box, show_faces=False)
viewer.add(box.frame, linewidth=3)
viewer.show()
