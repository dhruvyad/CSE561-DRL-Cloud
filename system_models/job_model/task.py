# tid = task id
# cpu = task cpu required
# mem = task mem required
# req_vms = task types of vms requested
# start_time = task scheduled start time
# deadline = task user set hard deadline
# exec_time = approximate tast execution time

class Task:
    def __init__(self, tid, cpu, mem, req_vms, start_time, deadline, exec_time):
        self.tid = tid
        self.cpu = cpu
        self.mem = mem
        self.req_vms = req_vms
        self.start_time = start_time
        self.deadline = deadline
        self.exec_time = exec_time