class PDController:
    def __init__(self, Kp, Kd):
        self.Kp = Kp
        self.Kd = Kd
        
    def compute_torque(self, theta, omega):
        torque = -self.Kp*theta - self.Kd*omega
        return torque