import math


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

import numpy as np

'''calculates the acceleration of an object given the force applied to it and its mass'''
def calculate_acceleration (F, m):
    if F <= 0 or m <= 0:
        raise ValueError ("invalid input")
    acceleration = F/m
    return acceleration

'''calculates the angular acceleration of an object given the torque applied to it and its moment of inertia'''
def calculate_angular_acceleration (tau, I):
    if I < 0:
        raise ValueError ("invalid input")
    angAcceleration = tau/I
    return angAcceleration

'''calculates the torque applied to an object given the force applied to it and the distance from the axis of rotation to the point where the force is applied'''
def calculate_torque (F_magnitude, F_direction, r):
    if F_magnitude < 0 or r < 0:
        raise ValueError ("invalid input")
    torque = r * np.sin(np.radians(F_direction)) * F_magnitude
    return torque

'''calculates the moment of inertia of an object given its mass and the distance from the axis of rotation to the center of mass of the object'''
def calculate_moment_of_inertia (m, r):
    if r < 0 or m < 0:
        raise ValueError ("invalid input")
    moment_of_inertia = m * r**2
    return moment_of_inertia

'''calculates the acceleration of the AUV in the 2D plane'''
def calculate_auv_acceleration (F_magnitude, F_angle, mass = 100, volume = 0.1, thruster_distance = 0.5):
    x_acc = F_magnitude * np.cos(F_angle)
    y_acc = F_magnitude * np.sin(F_angle)
    total_acc = np.array([x_acc, y_acc])
    thrusters = np.array ([F_magnitude])
    force = np.matmul([total_acc, thrusters])
    accl = np.array([force[0] / mass, force[1] / mass])
    return accl
    
'''calculates the angular acceleration of the AUV'''
def calculate_auv_angular_acceleration (F_magnitude, F_angle, intertia = 1, thruster_distance = 1):
    return calculate_torque(F_magnitude, F_angle, thruster_distance) / intertia

'''returns force components in reference to ROV plane'''
def rov_components (theta):
    array = np.array([[math.cos(theta), math.cos(theta), -math.cos(theta), -math.cos(theta)], 
                      [math.sin(theta, -math.sin(theta), -math.sin(theta), math.sin(theta))]])
    return array

def rotation_components (theta):
    array = np.array(
        [[(math.cos(theta), -math.sin(theta))], 
         [(math.sin(theta), math.cos(theta))]])
    return array

'''calculates the acceleration of the AUV in the 2D plane'''
def calculate_auv2_acceleration (T, alpha, theta, mass = 100):
     rov_rot = rotation_components (theta)
     force_array = np.matmul (rov_rot, T)
     acceleration = np.array([force_array[0] / mass, force_array[1] / mass])
     return np.matmul((rotation_components(theta)), acceleration)

'''calculates the angular acceleration of an rov with 4 thrusters'''

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia = 100):

    rov_rot = rotation_components(alpha)
    force_array = np.matmul(rov_rot, T)
    accl = np.array([force_array[0] / inertia, force_array[1] / inertia])
    r = math.sqrt(L**2 + l**2)
    magnitude = math.sqrt(accl[0] * accl[0] + accl[1] + accl[1])
    return calculate_torque(magnitude, alpha, r) / inertia
