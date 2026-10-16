# Task: Labyrinth
# Link: https://cses.fi/problemset/task/1194
# Topic: Graph Algorithms / BFS Shortest Path & Backtracking
# Complexity: O(N * M) time, O(N * M) auxiliary space

import sys
from collections import deque


def solve():
    input = sys.stdin.readline
    height, width = map(int, input().split())
    grid = []
    start = -1
    i = 0
    for _ in range(height):
        line = sys.stdin.readline().strip()
        grid.append(line)
        j = 0
        while (start == -1) and j < len(line):
            if line[j] == 'A':
                start = (i, j)
            j += 1
        i += 1

    pred = [[None] * width for _ in range(height)]
    bfs(start[0], start[1], pred, grid, height, width)


def bfs(start_i, start_j, pred, grid, height, width):
    queue = deque([(start_i, start_j)])
    pred[start_i][start_j] = 'A'
    end = (-1, -1)
    stop = False

    while queue and not stop:
        r, c = queue.popleft()

        for dr, dc, move in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:

                if pred[nr][nc] is None and (grid[nr][nc] == '.' or grid[nr][nc] == 'B'):
                    pred[nr][nc] = move
                    queue.append((nr, nc))

                    if grid[nr][nc] == 'B':
                        end = (nr, nc)
                        stop = True
                        break

    if stop:
        track_path(end, pred)
    else:
        print("NO")


def track_path(end, pred):
    i, j = end
    path = []
    step_back = {'U': (1, 0), 'D': (-1, 0), 'L': (0, 1), 'R': (0, -1)}
    while pred[i][j] != 'A':
        move = pred[i][j]
        path.append(move)
        di, dj = step_back[move]
        i += di
        j += dj

    path.reverse()

    print("YES")
    print(len(path))
    print("".join(path))


if __name__ == '__main__':
    solve()