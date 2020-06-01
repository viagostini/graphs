import pytest

from graph import Graph

def test_initialization():
    g = Graph()
    assert g.adj == {}
    assert len(g) == 0
    assert len(g.nodes) == 0
    assert len(g.edges) == 0

def test_add_node():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    assert len(g) == 2
    assert len(g.nodes) == 2
    assert g.adj == {1: set(), 2: set()}

def test_add_edge():
    g = Graph()
    g.add_node(1)
    g.add_edge(1, 2)
    assert len(g) == 2
    assert len(g.nodes) == 2
    assert len(g.edges) == 1
    assert g.adj == {1: set([2]), 2: set([1])}