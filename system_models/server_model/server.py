# sid = server id
# cpu = server cpu resources
# mem = server memory resources
# vms = list of number of vms available
# optimal_util = optimal server utilization
# static_pow = static server power consumption

class Server:
    def __init__(self, sid, cpu, mem, vms, static_pow, optimal_util):
        self.sid = sid
        self.cpu = cpu
        self.mem = mem
        self.vms = vms
        self.V = len(self.vms)
        self.used_vms = [] * self.V
        self.static_pow = static_pow
        self.optimal_util = optimal_util

    def utilization_rate(self):
        usage = 0
        for v in range(len(self.V)):
            usage += self.used_vms[v] * self.vms[v].cpu
        return usage / self.cpu