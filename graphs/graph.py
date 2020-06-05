class Graph:

    def __init__(self, directed=False, weighted=False):
        self.directed = directed
        self.weighted = weighted
        self.nodes = set()
        self.edges = set()
        self.adj = {}

    def __len__(self):
        return len(self.nodes)

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.add(node)
            self.adj[node] = set()

    def add_multiple_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_edge(self, node, other_node):
        assert not self.weighted, 'Cannot insert unweighted edge in weighted graph'

        self.add_multiple_nodes([node, other_node])

        self.adj[node].add(other_node)
        self.edges.add((node, other_node))

        if not self.directed:
            self.adj[other_node].add(node)
            self.edges.add((other_node, node))

    def add_multiple_edges(self, edges):
        for node, other_node in edges:
            self.add_edge(node, other_node)

    def add_weighted_edge(self, node, other_node, weight):
        assert self.weighted, 'Cannot insert weighted edge in unweighted graph'

        self.add_multiple_nodes([node, other_node])

        self.adj[node].add((other_node, weight))
        self.edges.add((node, other_node, weight))

        if not self.directed:
            self.adj[other_node].add((node, weight))
            self.edges.add((other_node, node, weight))

    def add_multiple_weighted_edges(self, edges):
        for node, other_node, weight in edges:
            self.add_weighted_edge(node, other_node, weight)

