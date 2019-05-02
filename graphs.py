class Graph:
    def __init__(self, V = None, E = None):
        self.V = V or []
        self.E = E or []

    @property
    def n(self):
        return len(self.V)
    
    @property
    def m(self):
        return len(self.E)

    def add_node(self, v):
        self.V.append(v)
    
    def add_edge(self, e):
        self.E.append(e)
