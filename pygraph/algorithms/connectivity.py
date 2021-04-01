from pygraph.algorithms.traversals import DepthFirstSearch
from pygraph.decorators import expected_graph_types
from pygraph.graph import Graph


@expected_graph_types(directed=False)
def count_components(graph: Graph) -> int:
    if not len(graph):
        raise RuntimeError("Graph is empty")

    dfs, visited, num_components = DepthFirstSearch(graph), set(), 0
    for node in graph:
        if node not in visited:
            dfs.clear()
            dfs.execute(node)
            visited = visited | dfs.visited
            num_components += 1

    return num_components


@expected_graph_types(directed=False)
def is_connected(graph: Graph) -> bool:
    return count_components(graph) == 1


"""     if not len(graph):
        raise RuntimeError("Graph is empty")

    source = next(iter(graph))
    dfs = DepthFirstSearch(graph)
    dfs.execute(source)

    return True if len(dfs.visited) == len(graph) else False """
