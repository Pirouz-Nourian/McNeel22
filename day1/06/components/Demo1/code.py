"""
Do something silly.
This component does nothing useful, it's only a minimal example.
    Args:
        x: X value
        y: Y value
        z: Z value
    Returns:
        a: The sum of all three values.
"""

from ghpythonlib.componentbase import executingcomponent as component


class MinimalComponent(component):
    def RunScript(self, x, y, z):
        self.Message = "COMPONENT test"
        return x + y + z
