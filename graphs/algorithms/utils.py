from collections import deque


def backtrace_path(start, end, parents):
    path = deque([end])

    node = end
    while node != start:
        path.appendleft(parents[node])
        node = parents[node]

    return list(path)