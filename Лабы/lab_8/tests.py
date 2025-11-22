import unittest
from unittest.mock import MagicMock, patch
import json
from task_1 import GraphReader, GraphWriter, Graph


class TestGraph(unittest.TestCase):
    def test_from_adjacency_matrix(self):  # тест преобразования матрицы смежности в список смежности
        adjacency_matrix = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        graph = Graph(adjacency_matrix)
        expected_adjacency_list = {
            0: [1],
            1: [0, 2],
            2: [1],
        }
        self.assertEqual(graph.adjacency_list, expected_adjacency_list)

    def test_to_edge_list(self):  # тест преобразования списка смежности в список рёбер
        adjacency_matrix = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        graph = Graph(adjacency_matrix)
        expected_edge_list = [(0, 1), (1, 2)]
        self.assertEqual(graph.to_edge_list(), expected_edge_list)

    def test_reverse_traversal(self):  # тест обратного обхода дерева
        adjacency_matrix = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        graph = Graph(adjacency_matrix)
        reverse_order = graph.reverse_traversal(0)
        self.assertEqual(reverse_order, [2, 1, 0])

    # ОТРИЦАТЕЛЬНЫЙ ТЕСТ 1: пустая матрица смежности
    def test_empty_adjacency_matrix(self):
        adjacency_matrix = []
        graph = Graph(adjacency_matrix)
        self.assertEqual(graph.adjacency_list, {})
        self.assertEqual(graph.to_edge_list(), [])

    # ОТРИЦАТЕЛЬНЫЙ ТЕСТ 2: обход с несуществующей вершиной
    def test_reverse_traversal_invalid_node(self):
        adjacency_matrix = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        graph = Graph(adjacency_matrix)
        # Вершина 10 не существует в графе
        reverse_order = graph.reverse_traversal(10)
        self.assertEqual(reverse_order, [10])


class TestGraphReaderWriter(unittest.TestCase):  # тест чтения матрицы смежности из файла с использованием заглушки
    def test_read_from_file(self):
        file_content = json.dumps([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

        with patch("builtins.open", new_callable=unittest.mock.mock_open, read_data=file_content) as mock_file:
            adjacency_matrix = GraphReader.read_from_file("fake_file.json")
            self.assertEqual(adjacency_matrix, [[0, 1, 1], [1, 0, 1], [1, 1, 0]])
            mock_file.assert_called_once_with("fake_file.json", "r")

    def test_write_to_file(self):  # тест записи списка рёбер в файл с использованием заглушки
        edge_list = [(0, 1), (1, 2)]

        with patch("builtins.open", new_callable=unittest.mock.mock_open) as mock_file:
            GraphWriter.write_to_file("fake_file.json", edge_list)
            mock_file.assert_called_once_with("fake_file.json", "w")
            mock_file().write.assert_called_once_with(json.dumps(edge_list))

    # ОТРИЦАТЕЛЬНЫЙ ТЕСТ 3: чтение несуществующего файла
    def test_read_from_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            GraphReader.read_from_file("nonexistent_file.json")

    # ОТРИЦАТЕЛЬНЫЙ ТЕСТ 4: чтение файла с некорректным JSON
    def test_read_from_file_invalid_json(self):
        file_content = "this is not a valid json"

        with patch("builtins.open", new_callable=unittest.mock.mock_open, read_data=file_content):
            with self.assertRaises(json.JSONDecodeError):
                GraphReader.read_from_file("fake_file.json")


class TestIntegration(unittest.TestCase):  # интеграционный тест взаимодействия Graph, GraphReader и GraphWriter
    def test_integration(self):
        file_content = json.dumps([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

        with patch("builtins.open", new_callable=unittest.mock.mock_open, read_data=file_content):
            adjacency_matrix = GraphReader.read_from_file("fake_file.json")

        graph = Graph(adjacency_matrix)
        edge_list = graph.to_edge_list()
        self.assertEqual(edge_list, [(0, 1), (0, 2), (1, 2)])

        with patch("builtins.open", new_callable=unittest.mock.mock_open) as mock_file:
            GraphWriter.write_to_file("fake_file.json", edge_list)
            mock_file.assert_called_once_with("fake_file.json", "w")
            mock_file().write.assert_called_once_with(json.dumps(edge_list))


if __name__ == '__main__':
    unittest.main()
