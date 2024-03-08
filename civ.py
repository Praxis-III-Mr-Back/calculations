import math
import pint
ureg = pint.UnitRegistry()

E_pvc = 3.5 * ureg.gigapascal
length = 0.5 * ureg.meter
radius =  1 * ureg.inch
thickness = 0.5 * ureg.inch
force = 1 * ureg.gram * ureg.meter / ureg.second**2

def pipe_area_moment_of_inertia(radius, thickness):
    return math.pi * (radius**4 - (radius - thickness)**4) / 64

def pipe_tip_deflection(length, radius, thickness, force, E):
    I = pipe_area_moment_of_inertia(radius, thickness)
    return (force * length**3) / (3 * E * I)


# print(pipe_area_moment_of_inertia(radius, thickness))
print(pipe_tip_deflection(length, radius, thickness, force, E_pvc).to(ureg.millimeter))