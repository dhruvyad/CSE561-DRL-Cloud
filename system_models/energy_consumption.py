# calculate the current energy consumption given
# servers and their used resources

class EnergyConsumption:
    def __init__(self, alpha, beta, servers):
        self.alpha = alpha
        self.beta = beta
        self.servers = servers
        self.M = len(self.servers)

    # calculate static power consumption of a given server
    def static_power(self, server):
        if(server.utilization_rate() > 0):
            return server.static_pow
        else:
            return 0

    # calculate dynamic power consumption of a given server
    def dynamic_power(self, server, alpha, beta):
        if(server.utilization() < server.optimal_util):
            return server.utilization_rate() * alpha
        else:
            return server.optimal_util * alpha + pow(server.utilization_rate() - server.optimal_util, 2) * beta

    # calculate the total power consumption of all servers
    def total_power(self):
        static_pow = 0
        dyn_pow = 0
        for m in range(self.M):
            static_pow += self.static_power(self.servers[m])
            dyn_pow += self.dynamic_power(self.servers[m], self.alpha[m], self.beta[m])
        return static_pow + dyn_pow