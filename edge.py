class Edge:
    def __init__(self, id, start_node, end_node, max_capacity, current_capacity=0):
        self.id = id
        self.start_node = start_node
        self.end_node = end_node
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity

    def add_to_current_capacity(self, new_capacity):
        if new_capacity <= self.max_capacity:
            self.current_capacity += new_capacity
        else:
            print("Error: New capacity exceeds maximum capacity")

    def decrease_capacity(self, new_capacity):
        if new_capacity - self.current_capacity > 0:
            self.current_capacity -= new_capacity
        else:
            self.current_capacity = 0 # Sets capacity to 0 ??

    def get_current_capacity(self):
        return self.current_capacity

    def get_start_node(self):
        return self.start_node

    def get_end_node(self):
        return self.end_node

    def get_max_capacity(self):
        return self.max_capacity
