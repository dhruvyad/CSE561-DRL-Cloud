class RealisticPrice:
    def __init__(self, energy_model, theta, RTP_l, RTP_h):
        self.energy_model = energy_model
        self.theta = theta
        self.RTP_l = RTP_l
        self.RTP_h = RTP_h

    def RTP(self):
        if(self.energy_model.total_power() < self.theta):
            return self.RTP_l
        else:
            return self.RTP_h
