# tasks = list of tasks
# dependencies list of edges between tasks

class Job:
    def __init__(self, tasks, dependencies):
        self.tasks = tasks
        self.dependecies = dependencies