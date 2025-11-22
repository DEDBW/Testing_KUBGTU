import json


class Graph:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.adjacency_list = self._matrix_to_list()

    def _matrix_to_list(self):
        adjacency_list = {}
        for i, row in enumerate(self.adjacency_matrix):
            adjacency_list[i] = [j for j, value in enumerate(row) if value == 1]
        return adjacency_list

    def to_edge_list(self):
        edges = set()
        for node, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                if (neighbor, node) not in edges:
                    edges.add((node, neighbor))
        return list(edges)

    def reverse_traversal(self, start_node):
        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            for neighbor in sorted(self.adjacency_list.get(node, [])):
                if neighbor not in visited:
                    dfs(neighbor)
            result.append(node)

        dfs(start_node)
        return result


class GraphReader:
    @staticmethod
    def read_from_file(filename):
        with open(filename, 'r') as file:
            return json.load(file)


class GraphWriter:
    @staticmethod
    def write_to_file(filename, data):
        with open(filename, 'w') as file:
            file.write(json.dumps(data))
