def depth_first_search(graph, node=None, visited=None):
    if node is None:
        node = next(iter(graph.nodes))

    if visited is None:
        visited = set()

    visited.add(node)
    for next_node in (graph.adj[node] - visited):
        depth_first_search(graph, next_node, visited)