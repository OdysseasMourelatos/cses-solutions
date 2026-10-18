# Task: Dice Combinations
# Link: https://cses.fi/problemset/task/1633
# Topic: Dynamic Programming / 1D DP (Counting Paths / Transitions)
# Complexity: O(N) time, O(N) auxiliary space

import sys

def solve():
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        for dice in range(1, 7):
            if i - dice >= 0:
                dp[i] = (dp[i] + dp[i - dice]) % (10 ** 9 + 7)

    print(dp[n])

if __name__ == '__main__':
    solve()