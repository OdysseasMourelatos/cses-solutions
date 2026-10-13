# Task: Distinct Numbers
# Link: https://cses.fi/problemset/task/1621
# Topic: Sorting and Searching (Array Sorting / Linear Scan)
# Complexity: O(N log N) time, O(N) space

import sys

def solve():
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    numbers.sort()
    distinct_numbers = 1
    for i in range(1, n):
        if numbers[i] != numbers[i - 1]:
            distinct_numbers+=1
    print(distinct_numbers)

if __name__ == '__main__':
    solve()