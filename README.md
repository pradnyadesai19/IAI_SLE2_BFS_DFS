# IAI SLE-2: BFS vs DFS Performance Analysis

## About

This project is part of SLE-2 for **02AML204 – Introduction to Artificial Intelligence**.

The project compares the performance of:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms are tested on the same **63-node binary-tree graph**.

## Profiling

Performance is measured using:

- Node count
- Execution time using `time.perf_counter()`
- `py-spy` profiling

Each case is repeated **50,000 times** to obtain stable timing results.

## Results

### BFS

| Case | Goal | Nodes | Time |
|---|---:|---:|---:|
| Best | 1 | 2 | 2.198 µs |
| Average | 15 | 16 | 16.507 µs |
| Worst | 62 | 63 | 43.022 µs |

### DFS

| Case | Goal | Nodes | Time |
|---|---:|---:|---:|
| Best | 2 | 2 | 2.643 µs |
| Average | 47 | 32 | 29.217 µs |
| Worst | 31 | 63 | 48.688 µs |

## Complexity

Both BFS and DFS have a theoretical time complexity of **O(V + E)** for the adjacency-list implementation.

## Files

- `bfs.py` – BFS implementation
- `dfs.py` – DFS implementation
- `profile_bfs.py` – BFS profiling
- `profile_dfs.py` – DFS profiling
- `bfs_profile.svg` – BFS flamegraph
- `dfs_profile.svg` – DFS flamegraph
- `ContributionLog.md` – Contribution log

## Student

**Pradnya Desai**  
**PRN:** 25UAM020