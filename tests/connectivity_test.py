import pytest

from pygraph.algorithms.connectivity import is_connected, count_components
from pygraph.graph import Graph


def test_is_connected():
    graph = Graph(
        {
            "São Paulo": {"Rio de Janeiro", "Paraná"},
            "Rio de Janeiro": {"São Paulo"},
            "Paraná": {"São Paulo"},
        },
        directed=False,
        weighted=False,
    )

    assert is_connected(graph)


def test_is_connected_false():
    graph = Graph(
        {
            "São Paulo": {"Rio de Janeiro", "Paraná"},
            "Rio de Janeiro": {"São Paulo"},
            "Paraná": {"São Paulo"},
            "Amazonas": set(),
        },
        directed=False,
        weighted=False,
    )

    assert not is_connected(graph)


def test_is_connected_raises_if_empty():
    graph = Graph(directed=False)

    with pytest.raises(RuntimeError):
        is_connected(graph)


def test_count_components_single():
    graph = Graph(
        {
            "São Paulo": {"Rio de Janeiro", "Paraná"},
            "Rio de Janeiro": {"São Paulo"},
            "Paraná": {"São Paulo"},
        },
        directed=False,
        weighted=False,
    )

    assert count_components(graph) == 1


def test_count_components_multiple():
    graph = Graph(
        {
            "São Paulo": {"Rio de Janeiro", "Paraná"},
            "Rio de Janeiro": {"São Paulo"},
            "Paraná": {"São Paulo"},
            "Amazonas": set(),
            "Ceará": set(),
        },
        directed=False,
        weighted=False,
    )

    assert count_components(graph) == 3


def test_count_components_raises_if_empty():
    graph = Graph(directed=False)

    with pytest.raises(RuntimeError):
        count_components(graph)