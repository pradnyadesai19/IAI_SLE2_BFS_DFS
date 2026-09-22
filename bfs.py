from collections import deque
import time


def create_graph(depth):
    graph = {}

    for i in range(2 ** depth - 1):
        left = 2 * i + 1
        right = 2 * i + 2

        graph[i] = []

        if left < 2 ** depth - 1:
            graph[i].append(left)

        if right < 2 ** depth - 1:
            graph[i].append(right)

    return graph


graph = create_graph(6)
start_node = 0


def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes_explored = 0

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            return nodes_explored

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return nodes_explored


cases = {
    "Best Case": 1,
    "Average Case": 15,
    "Worst Case": 62
}


if __name__ == "__main__":

    repetitions = 50000

    for case, goal_node in cases.items():

        bfs_times = []

        for i in range(3):

            start_time = time.perf_counter()

            for j in range(repetitions):
                bfs_nodes = bfs(graph, start_node, goal_node)

            bfs_time = (time.perf_counter() - start_time) / repetitions
            bfs_times.append(bfs_time)

        average_time = sum(bfs_times) / len(bfs_times)

        print("\n" + case)
        print("Goal node:", goal_node)
        print("BFS nodes explored:", bfs_nodes)
        print("BFS times:", bfs_times)
        print("BFS average time:", average_time)