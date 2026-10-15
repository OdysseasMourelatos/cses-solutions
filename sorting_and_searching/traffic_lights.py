# Task: Traffic Lights
# Link: https://cses.fi/problemset/task/1163
# Topic: Sorting & Searching / Offline Processing (Reverse Time & Linked List)
# Complexity: O(N log N) time, O(N) space

import sys


def solve():
    input = sys.stdin.readline
    street_len, n = map(int, input().split())
    lights = list(map(int, input().split()))

    all_points = sorted([0, street_len] + lights)

    left_of = {}
    right_of = {}

    max_gap = 0
    for i in range(len(all_points)):
        p = all_points[i]
        if i > 0:
            left_of[p] = all_points[i - 1]
            gap = p - all_points[i - 1]
            if gap > max_gap:
                max_gap = gap
        if i < len(all_points) - 1:
            right_of[p] = all_points[i + 1]

    ans = []
    for p in reversed(lights):
        ans.append(max_gap)

        L = left_of[p]
        R = right_of[p]

        new_gap = R - L
        if new_gap > max_gap:
            max_gap = new_gap

        right_of[L] = R
        left_of[R] = L

    ans.reverse()
    print(*(ans))


if __name__ == '__main__':
    solve()