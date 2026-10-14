# Task: Movie Festival
# Link: https://cses.fi/problemset/task/1628
# Topic: Sorting & Searching / Greedy (Interval Scheduling)
# Complexity: O(N log N) time, O(N) space

import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    starting_times = {}
    ending_times = {}
    for i in range(n):
        times = list(map(int, sys.stdin.readline().split()))
        starting_times[i] = times[0]
        ending_times[i] = times[1]
    ending_times = {k: v for k, v in sorted(ending_times.items(), key=lambda item: item[1])}
    picks = 0
    current_time = 0
    for key, value in ending_times.items():
        if starting_times[key] >= current_time:
            picks += 1
            current_time = ending_times[key]
    print(picks)

if __name__ == '__main__':
    solve()