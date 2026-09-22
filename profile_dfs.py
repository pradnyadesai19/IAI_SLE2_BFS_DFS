from dfs import dfs, graph, start_node

cases = {
    "Best Case": 2,
    "Average Case": 47,
    "Worst Case": 31
}

repetitions = 50000

for case, goal_node in cases.items():
    for i in range(repetitions):
        dfs(graph, start_node, goal_node)

    print(case, "completed")