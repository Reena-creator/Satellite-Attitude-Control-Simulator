from satellite import Satellite
from controller import PDController
from reaction_wheel import ReactionWheel

from disturbances import sinusoidal_disturbance

from performance_metrics import *
from visualization import *

import numpy as np
import matplotlib.pyplot as plt

# CREATE OBJECTS
satellite = Satellite(I_sat=10.0)
controller = PDController(Kp=10, Kd=20)
wheel = ReactionWheel(I_rw=0.1, omega_max=2.0)

# SIMULATION PARAMETERS
dt = 0.01
t_final = 30
dump_threshold = 1.8

# INITIAL CONDITIONS
theta = np.deg2rad(20)
omega_sat = 0.0
omega_rw = 0.0

# STORAGE
time = []
theta_history = []
omega_rw_history = []
torque_history = []

# SIMULATION LOOP
for t in np.arange(0, t_final, dt):
    torque_cmd = controller.compute_torque(theta, omega_sat)
    disturbance = sinusoidal_disturbance(t)
    domega_sat = (torque_cmd + disturbance)/satellite.I_sat
    domega_rw = (-torque_cmd)/wheel.I_rw
    omega_sat += domega_sat*dt
    omega_rw += domega_rw*dt
    theta += omega_sat*dt

    # saturation
    if omega_rw > wheel.omega_max:
        omega_rw = wheel.omega_max
    elif omega_rw < -wheel.omega_max:
        omega_rw = -wheel.omega_max

    # momentum dumping
    if abs(omega_rw) > dump_threshold:
        omega_rw *= 0.98

    # store
    time.append(t)
    theta_history.append(np.rad2deg(theta))
    omega_rw_history.append(omega_rw)
    torque_history.append(torque_cmd)

# METRICS
theta_array = np.array(theta_history)
time_array = np.array(time)
peak_time, peak_value = calculate_peak_time(theta_array, time_array)
overshoot = calculate_overshoot(theta_array)
rise_time = calculate_rise_time(theta_array, time_array)
settling_time = calculate_settling_time(theta_array, time_array)

print()
print("Peak Time =", peak_time)
print("Peak Value =", peak_value)
print("Overshoot =", overshoot)
print("Rise Time =", rise_time)
print("Settling Time =", settling_time)

# PLOTS
plot_theta(time, theta_history)
plot_wheel_speed(time, omega_rw_history)
plot_torque(time, torque_history)

plt.show()