import math
import pint
ureg = pint.UnitRegistry()

g = 9.81 * ureg.meter / ureg.second**2

def pipe_area_moment_of_inertia(radius, thickness):
    return math.pi * (radius**4 - (radius - thickness)**4) / 64

def pipe_tip_deflection(length, radius, thickness, force, E):
    I = pipe_area_moment_of_inertia(radius, thickness)
    return (force * length**3) / (3 * E * I)

### Tip deflection for 1 inch PVC on arms (1m), 200g
E_pvc = 3.5 * ureg.gigapascal # PVC
length = 1 * ureg.meter
radius =  1 * ureg.inch
thickness = 0.5 * ureg.inch
force = 200 * ureg.gram * ureg.meter / ureg.second**2
print("Deflection", round(pipe_tip_deflection(length, radius, thickness, force, E_pvc).to(ureg.millimeter), 3))

def torque(length, force):
    return length * force

def pipe_volume(radius, thickness, length):
    return math.pi * (radius**2 - (radius - thickness)**2) * length

def pipe_force(density, radius, thickness, length):
    return pipe_volume(radius, thickness, length) * density * g

def pipe_torque(density, radius, thickness, length, force):
    return torque(length / 2, pipe_force(density, radius, thickness, length))

### Required torque for 1 inch PVC on arms (1m), 200g
pvc_density = 1.38 * ureg.gram / ureg.centimeter**3 # PVC
length = 1 * ureg.meter
radius =  1 * ureg.inch
thickness = 0.5 * ureg.inch
tip_force = 200 * ureg.gram * ureg.meter / ureg.second**2
tip_torque = torque(length, force).to(ureg.newton * ureg.meter)
total_torque = pipe_torque(pvc_density, radius, thickness, length, tip_force) + tip_torque
print("Torque", round(total_torque, 3).to(ureg.kilogram_force * ureg.centimeter))