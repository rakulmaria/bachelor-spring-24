class Edge:
    def __init__(self, id, start_vertex, end_vertex, max_capacity, current_flow=0):
        self.id = id
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.max_capacity = max_capacity
        self.current_flow = current_flow

    def add_to_current_flow(self, new_flow):
        if new_flow <= self.max_capacity:
            self.current_flow += new_flow
        else:
            print("Error: New capacity exceeds maximum capacity")
