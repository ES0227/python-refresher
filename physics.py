import math
import matplotlib.pyplot as plt


"""calculates the buoyancy force exerted on an object submerged in water"""
g = 9.81


def calculate_buoyancy(v, density_fluid):
    if v <= 0:
        raise ValueError("invalid volume")
    if density_fluid <= 0:
        raise ValueError("invalid fluid density")
    buoyancy_force = density_fluid * v * g
    return buoyancy_force


"""determines whether or not the object will float or sink"""


def will_it_float(v, mass):
    if v < 0:
        raise ValueError("invalid volume")
    if mass < 0:
        raise ValueError("invalid mass")
    if 1000 * v * g * mass > g * mass:
        return True
    elif 1000 * v * g * mass == g * mass:
        return None
    else:
        return False


"""calculates the pressure exerted on an object at a given depth in water"""


def calculate_pressure(depth):
    if depth < 0:
        raise ValueError("invalid depth")
    pressure_at_surface = 101325
    pressure = 1000 * g * depth + pressure_at_surface

    return pressure


import numpy as np

"""calculates the acceleration of an object given the force applied to it and its mass"""


def calculate_acceleration(F, m):
    if F <= 0 or m <= 0:
        raise ValueError("invalid input")
    acceleration = F / m
    return acceleration


"""calculates the angular acceleration of an object given the torque applied to it and its moment of inertia"""


def calculate_angular_acceleration(tau, I):
    if I < 0:
        raise ValueError("invalid input")
    angAcceleration = tau / I
    return angAcceleration


"""calculates the torque applied to an object given the force applied to it and the distance from the axis of rotation to the point where the force is applied"""


def calculate_torque(F_magnitude, F_direction, r):
    if F_magnitude < 0 or r < 0:
        raise ValueError("invalid input")
    torque = r * np.sin(np.radians(F_direction)) * F_magnitude
    return torque


"""calculates the moment of inertia of an object given its mass and the distance from the axis of rotation to the center of mass of the object"""


def calculate_moment_of_inertia(m, r):
    if r < 0 or m < 0:
        raise ValueError("invalid input")
    moment_of_inertia = m * np.power(r, 2)  # r**2
    return moment_of_inertia


"""calculates the acceleration of the AUV in the 2D plane"""


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    if F_magnitude > 100:
        raise ValueError("the thruster can only apply a force up to 100N")
    x_acc = F_magnitude * np.cos(F_angle)
    y_acc = F_magnitude * np.sin(F_angle)
    total_acc = np.array([x_acc, y_acc])
    force = np.matmul(total_acc, F_magnitude)
    x_force = force[0] / mass
    y_force = force[1] / mass
    accl = np.array([[x_force], [y_force]])
    return accl
    # np.array([np.cos(F_angle), np.sin(F_angle)]*F_magnitude)


"""calculates the angular acceleration of the AUV"""


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, intertia=1, thruster_distance=1
):
    if F_magnitude < 0 or thruster_distance < 0:
        raise ValueError("invalid input")
    return calculate_torque(F_magnitude, F_angle, thruster_distance) / intertia


"""returns force components in reference to ROV plane"""


def rov_components(theta):
    array = np.array(
        [
            [math.cos(theta), math.cos(theta), -math.cos(theta), -math.cos(theta)],
            [math.sin(theta), -math.sin(theta), -math.sin(theta), math.sin(theta)],
        ]
    )
    return array


def rotation_components(theta):
    array = np.array(
        [[(math.cos(theta), -math.sin(theta))], [(math.sin(theta), math.cos(theta))]]
    )
    return array


"""calculates the acceleration of the AUV in the 2D plane"""


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    # if type(T) != np.array:
    # raise TypeError
    # if np.shape(T) != (1, 4):
    # raise ValueError("shape of T is not (1,4)")
    rov_rot = rov_components(alpha)
    force_array = np.dot(rov_rot, T)
    force_array = np.dot(rotation_components(theta), force_array)
    acceleration = np.array([force_array[0] / mass, force_array[1] / mass])
    return acceleration
    # return np.dot((rotation_components(theta)), acceleration)


"""calculates the angular acceleration of an rov with 4 thrusters"""


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    rov_rot = np.array([1, -1, 1, -1])
    force_array = np.multiply(rov_rot, T)
    torque = force_array * (L * np.sin(alpha) + l * np.cos(alpha))
    net_torque = np.sum(torque)
    return net_torque / inertia
    # r = math.sqrt(L**2 + l**2)
    # magnitude = math.sqrt(accl[0] * accl[0] + accl[1] * accl[1])
    # return calculate_torque(magnitude, alpha, r) / inertia


def simulate_auv2_motion(
    T, alpha, L, l, mass=100, intertia=100, dt=0.1, t_final=500, x0=0, y0=0, theta0=0
):
    t = np.arange(0, t_final, dt)
    a = np.tile(np.zeros_like(t), (2, 1))

    v = np.tile(np.zeros_like(t), (2, 1))

    angular_accl = calculate_auv2_angular_acceleration(T, alpha, L, l, 100)
    omega = np.zeros_like(t)
    omega[0] = 0
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    x[0] = x0
    y[0] = y0

    theta = np.zeros_like(t)
    theta[0] = theta0
    a[0][0] = calculate_auv2_acceleration(T, alpha, theta[0], mass=100)[0][0]
    a[1][0] = calculate_auv2_acceleration(T, alpha, theta[0], mass=100)[1][0]

    for i in range(1, len(t)):
        a[0][i] = calculate_auv2_acceleration(T, alpha, theta[i - 1], mass=100)[0][0]
        a[1][i] = calculate_auv2_acceleration(T, alpha, theta[i - 1], mass=100)[1][0]
        v[0][i] = (
            a[0][i - 1] * dt + v[0][i - 1]
        )  # taking the integral means adding the current slice to the sum of the previous slices
        v[1][i] = a[1][i - 1] * dt + v[1][i - 1]
        omega[i] = angular_accl * dt + omega[i - 1]
        theta[i] = omega[i - 1] * dt + theta[i - 1]
        x[i] = v[0][i - 1] * dt + x[i - 1]
        # position = integral of velocity, velocity = integral of acceleration
        y[i] = v[1][i - 1] * dt + y[i - 1]

    return (t, x, y, theta, v, omega, a)


def plot_auv2_motion(tup):
    plt.plot(
        tup[1], tup[2], label="x position"
    )  # tuple is short and convenient but may be hard to understand at first sight
    #plt.plot(tup[1], tup[2], label="y position")
    #plt.plot(tup[0], tup[3], label="theta angle")

    """plt.plot(tuple[0], tuple[4], label="velocity")
    plt.plot(tuple[0], tuple[5], label="angular velocity")
    plt.plot(tuple[0], tuple[6], label="acceleration")"""
    #print(tup[1])
    #print(tup[2])

    plt.xlabel("X_Position (m)")
    plt.ylabel("Y_Position (m)")
    plt.xlim([-200, 200])
    plt.ylim([-200, 200])
    plt.legend()
    plt.show()

    # np.zeros_like(time)
