"""Problem: CSES - Tasks and Deadlines (1630)

Topic: Greedy / Exchange Argument / Sorting
Complexity: O(N log N) time, O(N) space
Strategy: Maximize sum(d_i - f_i) = sum(d_i) - sum(f_i).
          Since sum(d_i) is constant regardless of execution order, maximizing reward
          is equivalent to minimizing sum(f_i). By the exchange argument (Shortest
          Processing Time first), scheduling tasks in ascending order of duration
          minimizes the cumulative finishing time penalty.
"""

import os
import sys

if os.path.exists('../cses_previous_exams/input.txt'):
  sys.stdin = open('../cses_previous_exams/input.txt', 'r')

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)

    tasks = int(next(it))

    tasks_info = []
    for _ in range(tasks):
        duration = int(next(it))
        deadline = int(next(it))
        tasks_info.append((duration, deadline))

    tasks_info.sort()
    finishing_time, reward = 0, 0
    for duration, deadline in tasks_info:
        finishing_time += duration
        reward += deadline - finishing_time

    print(reward)

if __name__ == '__main__':
  solve()