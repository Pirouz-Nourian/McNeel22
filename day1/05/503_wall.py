"""
This script must be executed in the Grasshopper Python Editor.

1. Drop a new GHPython editor component
2. Add input parameter `surface` and connect any rhino surface
3. Paste this script inside the editor and run
4. To visualize results, connect `a` out parameter to a `Draw` COMPAS component

"""
import math
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Vector
from compas_rhino.conversions import RhinoSurface
from compas.utilities import linspace

xsize = 0.0615
ysize = 0.02625
zsize = 0.0260
xgap = 0.0018
zgap = 0.0004

surface = RhinoSurface.from_guid(surface).to_compas()

a = []

wall_vertical_curve = surface.v_isocurve(0)
wall_height = wall_vertical_curve.length()
courses = int(math.ceil((wall_height / (zsize + zgap))))

for ri, row in enumerate(linspace(0, 1, courses)):
    _, u = wall_vertical_curve.rhino_curve.NormalizedLengthParameter(row)

    row_curve = surface.u_isocurve(u)
    row_length = row_curve.length()

    c = row_length / (xsize + xgap)
    col_count = int(math.ceil(c))
    linspaced_vector = list(linspace(0, 1, col_count))
    half_brick_offset = linspaced_vector[1] / 2

    for l in linspaced_vector:
        if ri % 2:
            l += half_brick_offset

        fits, col = row_curve.rhino_curve.NormalizedLengthParameter(l)
        if not fits:
            break

        point = row_curve.point_at(col)
        xaxis = row_curve.tangent_at(col)
        frame = Frame(point, xaxis, xaxis.cross(Vector.Zaxis()))

        brick = Box.from_diagonal([(-xsize / 2, -ysize / 2, 0), (xsize / 2, ysize / 2, -zsize)])
        brick.frame = frame
        a.append(brick)
