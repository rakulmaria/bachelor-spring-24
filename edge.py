class Edge:
    def __init__(self, id, start_node, end_node, max_capacity, current_flow=0):
        self.id = id
        self.start_node = start_node
        self.end_node = end_node
        self.max_capacity = max_capacity
        self.current_flow = current_flow

    def add_to_current_flow(self, new_flow):
        if new_flow <= self.max_capacity:
            self.current_flow += new_flow
        else:
            print("Error: New capacity exceeds maximum capacity")