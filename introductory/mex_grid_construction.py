# Task: Mex Grid Construction
# Link: https://cses.fi/problemset/task/3419
# Topic: Introductory Problems / Constructive Algorithms (MEX Pattern)
# Complexity: O(N^2 * K) time where K is max MEX value, O(N^2) space

import sys

def solve():
    n = int(sys.stdin.readline())
    matrix = []
    for i in range(n):
        matrix.append([0 for j in range(n)])
    available_numbers = [1]
    for i in range(n):
        for j in range(n):
            if i != j:
                left_elements = {matrix[i][r] for r in range(j)}
                above_elements = {matrix[r][j] for r in range(i)}
                found = False
                for number in available_numbers:
                    if number not in left_elements and number not in above_elements:
                        matrix[i][j] = number
                        found = True
                        break
                if not found:
                    number = available_numbers[-1] + 1
                    available_numbers.append(number)
                    matrix[i][j] = available_numbers[-1]

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

if __name__ == '__main__':
    solve()