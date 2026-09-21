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


graph = create_graph(14)

start_node = 0
goal_node = 2 ** 13 - 1


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

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_explored = 0

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            return nodes_explored

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)

    return nodes_explored

if __name__ == "__main__":
    bfs_times = []
    dfs_times = []

    for i in range(3):
        start_time = time.perf_counter()
        bfs_nodes = bfs(graph, start_node, goal_node)
        bfs_time = time.perf_counter() - start_time
        bfs_times.append(bfs_time)

        start_time = time.perf_counter()
        dfs_nodes = dfs(graph, start_node, goal_node)
        dfs_time = time.perf_counter() - start_time
        dfs_times.append(dfs_time)

    print("BFS nodes explored:", bfs_nodes)
    print("DFS nodes explored:", dfs_nodes)

    print("BFS times:", bfs_times)
    print("DFS times:", dfs_times)

    print("BFS average time:", sum(bfs_times) / len(bfs_times))
    print("DFS average time:", sum(dfs_times) / len(dfs_times))