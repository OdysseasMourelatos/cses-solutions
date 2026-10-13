# CSES Problem Set Solutions

Solutions to algorithmic problems from the [CSES Problem Set](https://cses.fi/problemset/), implemented in Python 3 / PyPy3 for ICPC (GRCPC/SEERC) preparation.

## Progress

| Category | Problem | Solution | Complexity |
| :--- | :--- | :--- | :--- |
| **Introductory** | [Weird Algorithm](https://cses.fi/problemset/task/1068) | [weird_algorithm.py](introductory/weird_algorithm.py) | $O(N)$ |
| **Sorting and Searching** | [Distinct Numbers](https://cses.fi/problemset/task/1621) | [distinct_numbers.py](sorting_and_searching/distinct_numbers.py) | $O(N \log N)$ |
| **Sorting and Searching** | [Ferris Wheel](https://cses.fi/problemset/task/1090) | [ferris_wheel.py](sorting_and_searching/ferris_wheel.py) | $O(N \log N)$ |
| **Graph Algorithms** | [Counting Rooms](https://cses.fi/problemset/task/1192) | *In Progress* | $O(N \cdot M)$ |

## Notes on Python for Competitive Programming
- Use `sys.stdin.readline` instead of `input()` for fast input parsing.
- Avoid native `set` or `dict` on adversary test cases; prefer sorting ($O(N \log N)$) or bitwise masks to prevent hash collision attacks ($O(N^2)$ TLE).
