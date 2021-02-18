# data -  the amount of data that needs to be delivered from parent task
# i to to child task j

class TaskEdge:
    def __init__(self, parent, child, data):
        self.parent = parent
        self.child = child
        self.data = data