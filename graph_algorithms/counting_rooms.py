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
            if grid[i][j] == '.':
                visited[i][j] = True
                up, down, left, right = find_moves(i, j, height, width)
                up_visited, down_visited, left_visited, right_visited = None, None, None, None
                if up is not False:
                    up_visited = visited[up[0]][up[1]]
                    if grid[up[0]][up[1]] == '.':
                        visited[up[0]][up[1]] = True
                if down is not False:
                    down_visited = visited[down[0]][down[1]]
                    if grid[down[0]][down[1]] == '.':
                        visited[down[0]][down[1]] = True
                if left is not False:
                    left_visited = visited[left[0]][left[1]]
                    if grid[left[0]][left[1]] == '.':
                        visited[left[0]][left[1]] = True
                if right is not False:
                    right_visited = visited[right[0]][right[1]]
                    if grid[right[0]][right[1]] == '.':
                        visited[right[0]][right[1]] = True

                if not up_visited and not down_visited and not left_visited and not right_visited:
                    print(i, j)
                    rooms += 1
    print(rooms)


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