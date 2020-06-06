from graphs.algorithms.traversals import depth_first_search


def is_connected(graph):
    assert not graph.directed, 'Use is_strongly_connected for directed graphs.'

    visited = set()
    depth_first_search(graph, visited=visited)

    return True if len(visited) == len(graph) else False


def is_strongly_connected(graph):
    raise NotImplementedError
