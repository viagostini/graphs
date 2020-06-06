from collections import deque

from graphs.algorithms.utils import backtrace_path


def bfs_shortest_path(graph, start, end):
    """
    Returns one (of the possibly many) shortest paths from start node
    to end node if one exists, None otherwise
    """
    assert not graph.weighted, 'This method will not work for weighted graphs.'

    parents = {}
    distances = {start: 0}

    queue = deque([start])
    while queue:
        node = queue.popleft()
        for next_node in (graph.adj[node] - distances.keys()):
            parents[next_node] = node
            distances[next_node] = distances[node] + 1
            if next_node == end:
                return backtrace_path(start, end, parents)
            queue.append(next_node)

    return None
