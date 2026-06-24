import numpy as np

def calculate_peak_time(theta_array, time_array):
    peak_index = np.argmin(theta_array)
    peak_time = time_array[peak_index]
    peak_value = theta_array[peak_index]
    return peak_time, peak_value

def calculate_overshoot(theta_array, initial_angle=20):
    peak_value = np.min(theta_array)
    overshoot = abs(peak_value)
    percent_os = (overshoot / initial_angle)*100
    return percent_os

def calculate_rise_time(theta_array, time_array):
    rise_index = np.where(np.abs(theta_array)<2)[0][0]
    rise_time = time_array[rise_index]
    return rise_time

def calculate_settling_time(theta_array, time_array):
    band = 0.4
    settling_time = None
    for i in range(len(theta_array)):
        if np.all(np.abs(theta_array[i:])<band):
            settling_time = time_array[i]
            break
    return settling_time
