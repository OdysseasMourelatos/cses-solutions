import sys

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
        while (start== -1) and j < len(line):
            if line[j] == 'A':
                start = (i, j)
            j+=1
        i+=1

    visited = [[False] * width for _ in range(height)]
    pred = [[0] * width for _ in range(height)]
    bfs(start[0], start[1], visited, pred, grid, height, width)

from collections import deque

def bfs(start_i, start_j, visited, pred, grid, height, width):
    queue = deque([(start_i, start_j)])
    path = [(start_i, start_j)]
    visited[start_i][start_j] = True
    pred[start_i][start_j] = 'A'
    end = (-1, -1)
    stop = False
    description = ""
    while queue and not stop:
        r, c = queue.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:
                if not visited[nr][nc] and (grid[nr][nc] == '.' or grid[nr][nc] == 'B'):
                    if (dr, dc) == (-1, 0):
                        description = "U"
                    elif (dr, dc) == (1, 0):
                        description = "D"
                    elif (dr, dc) == (0, -1):
                        description = "L"
                    elif (dr, dc) == (0, 1):
                        description = "R"
                    visited[nr][nc] = True
                    pred[nr][nc] = (r, c, description)
                    queue.append((nr, nc))
                    path.append((nr, nc))
                    if grid[nr][nc] == 'B':
                        end = (nr, nc)
                        stop = True
    if stop:
        track_path(end, pred)
    else:
        print("NO")

def track_path(end, pred):
    i = end[0]
    j = end[1]
    path = []
    while pred[i][j] != 'A':
        i, j, description = pred[i][j]
        path.append(description)
    path.reverse()

    print("YES")
    print(len(path))
    print(*path, sep='')

if __name__ == '__main__':
    solve()