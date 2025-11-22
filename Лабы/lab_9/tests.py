import unittest
from unittest.mock import MagicMock, patch
from task_1 import Graph, GraphReader, GraphWriter


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.adjacency_matrix = [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
        ]
        self.graph = Graph(self.adjacency_matrix)

    def test_matrix_to_list(self):
        expected_list = {
            0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1],
            3: [1],
        }
        self.assertEqual(self.graph.adjacency_list, expected_list)

    def test_to_edge_list(self):
        expected_edges = [(0, 1), (0, 2), (1, 2), (1, 3)]
        self.assertEqual(sorted(self.graph.to_edge_list()), sorted(expected_edges))

    def test_reverse_traversal(self):
        expected_order = [2, 3, 1, 0]
        self.assertEqual(self.graph.reverse_traversal(0), expected_order)


class TestGraphIO(unittest.TestCase):
    @patch('task_1.GraphReader.read_from_file')
    def test_read_from_file(self, mock_read_from_file):
        mock_read_from_file.return_value = [[0, 1], [1, 0]]
        result = GraphReader.read_from_file("mocked_file.json")
        self.assertEqual(result, [[0, 1], [1, 0]])
        mock_read_from_file.assert_called_once_with("mocked_file.json")

    @patch('task_1.GraphWriter.write_to_file')
    def test_write_to_file(self, mock_write_to_file):
        data = [(0, 1), (1, 2)]
        GraphWriter.write_to_file("mocked_file.json", data)
        mock_write_to_file.assert_called_once_with("mocked_file.json", data)
