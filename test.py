import networkx as nx
import unittest

class ShortestPathNetworkXTest(unittest.TestCase):

    def bfs_shortest_paths(self, graph, start):
        if not graph:  # Если граф пуст
            raise nx.NetworkXError(f"The node {start} is not in the graph.")
        return nx.single_source_shortest_path_length(graph, start)

    def test_connected_graph(self):
        # Создаём связный граф
        graph = nx.Graph()
        graph.add_edges_from([("A", "B"), ("B", "C")])

        # Проверяем кратчайшие расстояния
        distances = self.bfs_shortest_paths(graph, "A")
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 1)
        self.assertEqual(distances["C"], 2)

    def test_disconnected_graph(self):
        # Создаём неразвязный граф
        graph = nx.Graph()
        graph.add_edges_from([("A", "B")])
        graph.add_node("C")

        # Проверяем кратчайшие расстояния
        distances = self.bfs_shortest_paths(graph, "A")
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 1)
        self.assertNotIn("C", distances)  # Вершина "C" недостижима

    def test_single_node_graph(self):
        # Создаём граф из одной вершины
        graph = nx.Graph()
        graph.add_node("A")

        # Проверяем кратчайшие расстояния
        distances = self.bfs_shortest_paths(graph, "A")
        self.assertEqual(distances["A"], 0)

    def test_cyclic_graph(self):
        # Создаём граф с циклом
        graph = nx.Graph()
        graph.add_edges_from([("A", "B"), ("B", "C"), ("C", "A")])

        # Проверяем кратчайшие расстояния
        distances = self.bfs_shortest_paths(graph, "A")
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 1)
        self.assertEqual(distances["C"], 1)

    def test_empty_graph(self):
        # Создаём пустой граф
        graph = nx.Graph()

        # Проверяем, что вызов метода с несуществующей вершиной вызывает исключение
        with self.assertRaises(nx.NetworkXError) as context:
            self.bfs_shortest_paths(graph, "A")

        self.assertEqual(str(context.exception), "The node A is not in the graph.")

if __name__ == '__main__':
    unittest.main()