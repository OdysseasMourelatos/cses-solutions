"""
Problem: E. javelins (GRCPC / Practice)
Approach: Exchange Argument (Greedy sort by fatigue coefficient descending)
          + 0-1 Knapsack DP inversion (dp[j] = min energy for exactly j targets)
Time Complexity: O(N log N + N^2) [~5*10^7 operations -> OK on PyPy3]
Space Complexity: O(N) [1D DP array]
"""

import os
import sys

if os.path.exists('input.txt'):
  sys.stdin = open('input.txt', 'r')

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    targets = int(data[0])
    energy = int(data[1])

    targets_info = []
    for i in range(targets):
        base_difficulty = int(data[2 + i])
        fatigue_coefficient = int(data[2 + i + targets])
        targets_info.append((base_difficulty, fatigue_coefficient))

    targets_info.sort(key=lambda x: x[1], reverse=True)
    dp = [float('inf')] * (targets + 1)
    dp[0] = 0

    i = 1

    for base_difficulty, fatigue_coefficient in targets_info:
        for j in range(i, 0, -1):
            energy_cost = base_difficulty + (j-1) * fatigue_coefficient
            dp[j] = min(dp[j], dp[j-1] + energy_cost)
        i+=1

    for j in range(targets, -1, -1):
        if dp[j] <= energy:
            print(j, dp[j])
            break

if __name__ == '__main__':
  solve()