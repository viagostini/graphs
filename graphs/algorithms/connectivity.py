from graphs.algorithms.traversals import depth_first_search
from graphs.algorithms.decorators import expected_graph_type


@expected_graph_type(directed=False)
def connected_components(graph):
    visited = set()
    for node in graph.nodes:
        if node not in visited:
            component = depth_first_search(graph, node)
            visited.update(component)
            yield component


@expected_graph_type(directed=False)
def is_connected(graph):
    visited = depth_first_search(graph)
    return True if len(visited) == len(graph) else False

