import pytest
from task_1 import Graph, GraphReader, GraphWriter
from fluent_assertions import FluentAssertions as fa

@pytest.fixture
def example_graph():
    adjacency_matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
    ]
    return Graph(adjacency_matrix)


def test_matrix_to_list(example_graph):
    adjacency_list = example_graph.adjacency_list
    assert adjacency_list == {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1],
    }, "Adjacency list should match expected structure."


def test_to_edge_list(example_graph):
    edge_list = example_graph.to_edge_list()
    expected_edges = [(0, 1), (0, 2), (1, 2), (1, 3)]
    assert sorted(edge_list) == sorted(expected_edges), "Edge list should match expected edges."


def test_reverse_traversal(example_graph):
    traversal = example_graph.reverse_traversal(0)
    expected_traversal = [2, 3, 1, 0]
    assert traversal == expected_traversal, "Reverse traversal should match expected order."


def test_graph_reader_and_writer(tmp_path):
    adjacency_matrix = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ]
    graph = Graph(adjacency_matrix)

    # Write edges to file
    edge_list = graph.to_edge_list()
    test_file = tmp_path / "test_edges.json"
    GraphWriter.write_to_file(test_file, edge_list)

    # Read edges back
    loaded_edges = GraphReader.read_from_file(test_file)
    loaded_edges = [tuple(edge) for edge in loaded_edges]
    assert edge_list == loaded_edges, "Edges loaded from file should match written edges."

def test_to_edge_list_with_fluent_assertions(example_graph):
    edge_list = example_graph.to_edge_list()
    expected_edges = [(0, 1), (0, 2), (1, 2), (1, 3)]
    assert sorted(edge_list) == sorted(expected_edges), "Edge list should match expected edges."
    fa.assert_equal(edge_list, expected_edges, "Edge list mismatch")
