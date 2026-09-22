from bfs import bfs, graph, start_node

cases = {
    "Best Case": 1,
    "Average Case": 15,
    "Worst Case": 62
}

repetitions = 50000

for case, goal_node in cases.items():
    for i in range(repetitions):
        bfs(graph, start_node, goal_node)

    print(case, "completed")