import pytest
from fluent_assertions import FluentAssertions as fa
from task_1 import Graph, GraphReader, GraphWriter


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
    expected_list = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1],
    }
    fa.assert_equal(example_graph.adjacency_list, expected_list, "Неправильный список смежности")


def test_to_edge_list(example_graph):
    expected_edges = [(0, 1), (0, 2), (1, 2), (1, 3)]
    edge_list = example_graph.to_edge_list()
    fa.assert_equal(sorted(edge_list), sorted(expected_edges), "Неправильный список рёбер")


def test_reverse_traversal(example_graph):
    expected_order = [2, 3, 1, 0]
    reverse_order = example_graph.reverse_traversal(0)
    fa.assert_equal(reverse_order, expected_order, "Обратный обход неправильный")


def test_graph_reader_and_writer(tmp_path):
    filename = tmp_path / "test.json"
    data = [[0, 1], [1, 2]]

    GraphWriter.write_to_file(filename, data)
    loaded_data = GraphReader.read_from_file(filename)

    fa.assert_equal(loaded_data, data, "Данные, загруженные из файла, не совпадают")


# Дополнительные тесты
def test_empty_graph():
    empty_graph = Graph([])
    fa.assert_equal(empty_graph.adjacency_list, {}, "Список смежности для пустого графа должен быть пустым")


def test_single_node_graph():
    single_node_graph = Graph([[0]])
    fa.assert_equal(single_node_graph.adjacency_list, {0: []}, "Список смежности для графа из одной вершины некорректен")


def test_no_edges():
    graph = Graph([[0, 0], [0, 0]])
    expected_list = {0: [], 1: []}
    fa.assert_equal(graph.adjacency_list, expected_list, "Список смежности для графа без рёбер некорректен")
