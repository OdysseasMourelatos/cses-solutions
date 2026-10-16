import sys

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
                visited[i][j] = True
                rooms += 1
                bfs(i, j, visited, grid, height, width)
    print(rooms)

def bfs(i, j, visited, grid, height, width):
    up, down, left, right = find_moves(i, j, height, width)
    if up is not False and not visited[up[0]][up[1]] and grid[up[0]][up[1]] == '.':
        visited[up[0]][up[1]] = True
        bfs(up[0], up[1], visited, grid, height, width)
    if down is not False and not visited[down[0]][down[1]] and grid[down[0]][down[1]] == '.':
        visited[down[0]][down[1]] = True
        bfs(down[0], down[1], visited, grid, height, width)
    if left is not False and not visited[left[0]][left[1]] and grid[left[0]][left[1]] == '.':
        visited[left[0]][left[1]] = True
        bfs(left[0], left[1], visited, grid, height, width)
    if right is not False and not visited[right[0]][right[1]] and grid[right[0]][right[1]] == '.':
        visited[right[0]][right[1]] = True
        bfs(right[0], right[1], visited, grid, height, width)

def find_moves(i, j, height, width):
    up, down, left, right = False, False, False, False
    if i > 0:
        up = (i - 1, j)
    if i < height - 1:
        down = (i + 1, j)
    if j > 0:
        left = (i, j - 1)
    if j < width - 1:
        right = (i, j + 1)
    return up, down, left, right

if __name__ == '__main__':
    solve()