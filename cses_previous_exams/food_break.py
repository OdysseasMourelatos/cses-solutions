"""
Contest: GRCPC 2025
Problem: B. foodbreak
Topic: Sorting / Intervals / Greedy
Complexity: O(N log N) time, O(N) space
Strategy: Sort presentation intervals by start time. Track running maximum ending time
          to compute true disjoint gaps between overlapping intervals and boundaries [0, T].
"""

import sys

def solve():
    input = sys.stdin.readline
    num_presentations, len_day = map(int, input().split())
    times = []
    for i in range(num_presentations):
        presentation_time = list(map(int, sys.stdin.readline().split()))
        times.append(presentation_time)

    times.sort(key = lambda t: t[0])
    max_ending_time = 0
    max_gap = times[0][0]
    for i in range(0, len(times) -1):
        e_i = times[i][1]
        s_i1 = times[i+1][0]
        max_ending_time = max(max_ending_time, e_i)
        if e_i >= s_i1:
            continue
        gap = s_i1 - max_ending_time
        max_gap = max(max_gap, gap)

    max_ending_time = max(max_ending_time, times[-1][1])
    max_gap = max(max_gap, len_day - max_ending_time)
    print(max_gap)

if __name__ == '__main__':
    solve()