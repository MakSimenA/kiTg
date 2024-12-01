import networkx as nx
from collections import deque

def bfs_shortest_paths(graph, start):
    # Словарь для хранения кратчайших расстояний
    distances = {vertex: float('inf') for vertex in graph.nodes}
    distances[start] = 0  # Расстояние до начальной вершины = 0

    # Очередь для BFS
    queue = deque([start])

    # BFS
    while queue:
        current = queue.popleft()
        current_distance = distances[current]

        # Обрабатываем всех соседей текущей вершины
        for neighbor in graph.neighbors(current):
            # Если сосед ещё не посещён
            if distances[neighbor] == float('inf'):
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)  # Добавляем соседа в очередь

    return distances  # Возвращаем словарь с кратчайшими расстояниями


if __name__ == "__main__":
    # Создаём граф
    graph = nx.Graph()

    # Добавляем вершины
    graph.add_nodes_from(["A", "B", "C", "D", "E"])

    # Добавляем рёбра (они автоматически имеют единичный вес)
    graph.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")])

    # Запускаем алгоритм
    distances = bfs_shortest_paths(graph, "A")

    # Вывод результатов
    print("Кратчайшие расстояния от вершины A:")
    for vertex, distance in distances.items():
        print(f"Вершина {vertex}: {'недостижима' if distance == float('inf') else distance}")