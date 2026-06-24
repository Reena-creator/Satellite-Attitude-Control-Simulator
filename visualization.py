import matplotlib.pyplot as plt

def plot_theta(time, theta):

    plt.figure()
    plt.plot(time, theta)
    plt.grid()
    plt.xlabel("Time (s)")
    plt.ylabel("Theta (deg)")
    plt.title("Attitude Response")

    plt.savefig("results/attitude_response.png")


def plot_wheel_speed(time, omega_rw):

    plt.figure()
    plt.plot(time, omega_rw)
    plt.grid()
    plt.xlabel("Time (s)")
    plt.ylabel("Wheel Speed (rad/s)")
    plt.title("Reaction Wheel Speed")

    plt.savefig("results/wheel_speed.png")

def plot_torque(time, torque):

    plt.figure()
    plt.plot(time, torque)
    plt.grid()
    plt.xlabel("Time (s)")
    plt.ylabel("Torque (Nm)")
    plt.title("Control Torque")

    plt.savefig("results/control_torque.png")