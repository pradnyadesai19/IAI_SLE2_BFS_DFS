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
goal_node = 1


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

    dfs_times = []
    repetitions = 50000

    for i in range(3):
        start_time = time.perf_counter()

        for j in range(repetitions):
            dfs_nodes = dfs(graph, start_node, goal_node)

        dfs_time = (time.perf_counter() - start_time) / repetitions
        dfs_times.append(dfs_time)

    print("DFS nodes explored:", dfs_nodes)
    print("DFS times:", dfs_times)
    print("DFS average time:", sum(dfs_times) / len(dfs_times))
    