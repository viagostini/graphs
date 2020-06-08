import pytest

from graphs.graph import Graph
from graphs.algorithms.decorators import expected_graph_type


@pytest.fixture
def graph_types():
    graphFF = Graph(directed=False, weighted=False)
    graphFT = Graph(directed=False, weighted=True)
    graphTF = Graph(directed=True, weighted=False)
    graphTT = Graph(directed=True, weighted=True)

    return graphFF, graphFT, graphTF, graphTT


def test_expected_graph_type_decorator_undirected(graph_types):
    @expected_graph_type(directed=False)
    def func(graph):
        return True

    graphFF, graphFT, graphTF, graphTT = graph_types

    assert func(graphFF)
    assert func(graphFT)

    with pytest.raises(KeyError):
        assert func(graphTF)

    with pytest.raises(KeyError):
        assert func(graphTT)


def test_expected_graph_type_decorator_directed(graph_types):
    @expected_graph_type(directed=True)
    def func(graph):
        return True

    graphFF, graphFT, graphTF, graphTT = graph_types

    assert func(graphTF)
    assert func(graphTT)

    with pytest.raises(KeyError):
        assert func(graphFF)

    with pytest.raises(KeyError):
        assert func(graphFT)


def test_expected_graph_type_decorator_unweighted(graph_types):
    @expected_graph_type(weighted=False)
    def func(graph):
        return True

    graphFF, graphFT, graphTF, graphTT = graph_types

    assert func(graphFF)
    assert func(graphTF)

    with pytest.raises(KeyError):
        assert func(graphFT)

    with pytest.raises(KeyError):
        assert func(graphTT)


def test_expected_graph_type_decorator_weighted(graph_types):
    @expected_graph_type(weighted=True)
    def func(graph):
        return True

    graphFF, graphFT, graphTF, graphTT = graph_types

    assert func(graphFT)
    assert func(graphTT)

    with pytest.raises(KeyError):
        assert func(graphFF)

    with pytest.raises(KeyError):
        assert func(graphTF)


def test_expected_graph_type_decorator_mixed(graph_types):
    @expected_graph_type(directed=False, weighted=True)
    def func(graph):
        return True

    graphFF, graphFT, graphTF, graphTT = graph_types

    assert func(graphFT)

    with pytest.raises(KeyError):
        assert func(graphTT)

    with pytest.raises(KeyError):
        assert func(graphFF)

    with pytest.raises(KeyError):
        assert func(graphTF)
        