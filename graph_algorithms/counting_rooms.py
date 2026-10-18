# Task: Counting Rooms
# Link: https://cses.fi/problemset/task/1192
# Topic: Graph Algorithms / Connected Components & Grid BFS
# Complexity: O(N * M) time, O(N * M) space

import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    height, width = map(int, input().split())
    grid = []
    for _ in range(height):
        grid.append(sys.stdin.readline().strip())

    visited = [[False] * width for _ in range(height)]
    rooms = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == '.' and not visited[i][j]:
                rooms += 1
                bfs(i, j, visited, grid, height, width)
    print(rooms)

def bfs(start_i, start_j, visited, grid, height, width):
    queue = deque([(start_i, start_j)])
    visited[start_i][start_j] = True

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:
                if not visited[nr][nc] and grid[nr][nc] == '.':
                    visited[nr][nc] = True
                    queue.append((nr, nc))

if __name__ == '__main__':
    solve()