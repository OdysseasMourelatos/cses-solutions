# CSES Problem Set Solutions

Solutions to algorithmic problems from the [CSES Problem Set](https://cses.fi/problemset/), implemented in Python 3 / PyPy3 for ICPC (GRCPC/SEERC) preparation.

## Progress

### Introductory Problems
| Problem | Solution | Complexity | Key Technique |
| :--- | :--- | :--- | :--- |
| [Weird Algorithm](https://cses.fi/problemset/task/1068) | [weird_algorithm.py](introductory/weird_algorithm.py) | $O(N)$ | Collatz Simulation |
| [Bit Strings](https://cses.fi/problemset/task/1617) | [bit_strings.py](introductory/bit_strings.py) | $O(\log N)$ | Modular Exponentiation (`pow(2, n, MOD)`) |
| [Palindrome Reorder](https://cses.fi/problemset/task/1755) | [palindrome_reorder.py](introductory/palindrome_reorder.py) | $O(N)$ | Frequency Counting / Parity Check |
| [Apple Division](https://cses.fi/problemset/task/1623) | [apple_division.py](introductory/apple_division.py) | $O(2^N)$ | Complete Search / Bitmask Subset Sum |
| Mex Grid Construction | [mex_grid_construction.py](introductory/mex_grid_construction.py) | $O(N \cdot M)$ | Constructive Matrix / Mex Property |

---

### Sorting and Searching
| Problem | Solution | Complexity | Key Technique |
| :--- | :--- | :--- | :--- |
| [Distinct Numbers](https://cses.fi/problemset/task/1621) | [distinct_numbers.py](sorting_and_searching/distinct_numbers.py) | $O(N \log N)$ | Sorting vs Hash-table Anti-hash |
| [Ferris Wheel](https://cses.fi/problemset/task/1090) | [ferris_wheel.py](sorting_and_searching/ferris_wheel.py) | $O(N \log N)$ | Greedy Two Pointers |
| [Movie Festival](https://cses.fi/problemset/task/1629) | [movie_festival.py](sorting_and_searching/movie_festival.py) | $O(N \log N)$ | Interval Scheduling (Sort by End Time) |
| [Playlist](https://cses.fi/problemset/task/1676) | [playlist.py](sorting_and_searching/playlist.py) | $O(N)$ | Two Pointers / Sliding Window |
| [Traffic Lights](https://cses.fi/problemset/task/1163) | [traffic_lights.py](sorting_and_searching/traffic_lights.py) | $O(N \log N)$ | Ordered Maintenance / `bisect` & Segment Tracking |

---

### Graph Algorithms
| Problem | Solution | Complexity | Key Technique |
| :--- | :--- | :--- | :--- |
| [Counting Rooms](https://cses.fi/problemset/task/1192) | [counting_rooms.py](graph_algorithms/counting_rooms.py) | $O(N \cdot M)$ | Iterative BFS (`deque`) / Connected Components |
| [Labyrinth](https://cses.fi/problemset/task/1194) | [labyrinth.py](graph_algorithms/labyrinth.py) | $O(N \cdot M)$ | BFS Shortest Path / Character-based Parent Tracking |
| [Message Route](https://cses.fi/problemset/task/1193) | [message_route.py](graph_algorithms/message_route.py) | $O(V + E)$ | BFS / Unweighted Shortest Path Reconstruction |
| [Course Schedule](https://cses.fi/problemset/task/1679) | [course_schedule.py](graph_algorithms/course_schedule.py) | $O(V + E)$ | Topological Sort (Kahn's Algorithm via In-degrees) |

---

## Notes on Python for Competitive Programming

### 1. I/O & Recursion Overhead
- **Fast I/O:** Always map `sys.stdin.readline` to `input` for handling up to $10^6$ input elements under 0.2s.
- **Iteration over Recursion:** Prefer iterative structures (`while queue:`) with `collections.deque` over recursive DFS to avoid Python call-stack exhaustion (`RecursionError`) and high stack-frame allocation costs on large graphs ($V > 1000$).

### 2. Memory Allocations & TLE Avoidance
- **Avoid Heavy Tuples in Tight Loops:** Storing 3-tuples `(r, c, move)` in 2D grids with $10^6$ states triggers severe Garbage Collection penalties. Store primitive scalars (characters like `'U'`, `'D'` or integer codes) instead and derive previous states arithmetically.
- **State Array Consolidation:** Reuse predecessor tables (`pred`) to track the visited state simultaneously (e.g., `None` implies unvisited) to cut auxiliary memory in half.
- **Direction Vectors:** Use static vectors `[(-1, 0, 'U'), (1, 0, 'D'), ...]` to unify neighbor discovery and eliminate branching cascades.
- **Adjacency Lists:** Prefer `adj = [[] for _ in range(n + 1)]` indexed lookups over hash tables (`dict`) for consecutive node labels ($1 \dots N$).
