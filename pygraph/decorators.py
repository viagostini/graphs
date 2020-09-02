from functools import wraps


def expected_graph_types(**expected_types):
    def decorator_expected_graph_type(func):
        @wraps(func)
        def wrapper_expected_graph_type(*args, **kwargs):
            graph = args[0]

            if (
                "directed" in expected_types
                and graph.directed != expected_types["directed"]
            ):
                raise RuntimeError("Graph doesn't match expected types")

            if (
                "weighted" in expected_types
                and graph.weighted != expected_types["weighted"]
            ):
                raise RuntimeError("Graph doesn't match expected types")

            value = func(*args, **kwargs)
            return value

        return wrapper_expected_graph_type

    return decorator_expected_graph_type