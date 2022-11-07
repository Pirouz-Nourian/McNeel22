import os
import compas
from compas_view2.app import App
# =============================================================================
# Import
# =============================================================================

filepath = os.path.join(os.path.dirname(__file__), "session.json")
data = compas.json_load(filepath)

curve = data["curve"]
box = data["box"]

print(curve)
print(box)

viewer=App()
viewer.add(curve.to_polyline())
viewer.show()