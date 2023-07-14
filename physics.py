'''calculates the buoyancy force exerted on an object submerged in water'''
g = 9.81
def calculate_buoyancy (v, density_fluid):
    if v <= 0:
        raise ValueError("invalid volume")
    if density_fluid <= 0:
        raise ValueError("invalid fluid density")
    buoyancy_force = density_fluid * v * g
    return buoyancy_force

'''determines whether or not the object will float or sink'''
def will_it_float (v, mass): 
    if v < 0:
        raise ValueError("invalid volume")
    if  mass < 0:
        raise ValueError("invalid mass")
    if 1000 * v * g * mass > g * mass:
        return True
    elif 1000 * v * g * mass == g * mass:
        return None
    else:
        return False

'''calculates the pressure exerted on an object at a given depth in water'''
def calculate_pressure (depth):
    pressure_at_surface = 101325
    depth = abs(depth)
    pressure = 1000 * g * depth + pressure_at_surface
    return pressure

    