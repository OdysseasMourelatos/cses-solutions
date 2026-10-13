# Task: Ferris Wheel
# Link: https://cses.fi/problemset/task/1090
# Topic: Sorting and Searching (Greedy / Two Pointers)
# Complexity: O(N log N) time, O(N) space

import sys

def solve():
    input = sys.stdin.readline
    n, max_weight = map(int, input().split())
    weights = list(map(int, sys.stdin.readline().split()))
    weights.sort()
    gondolas = 0
    smallest_index = 0
    biggest_index = n - 1
    while smallest_index <= biggest_index:
        if weights[biggest_index] + weights[smallest_index] > max_weight:
            biggest_index -= 1
        else:
            biggest_index -= 1
            smallest_index += 1
        gondolas += 1
    print(gondolas)

if __name__ == '__main__':
    solve()