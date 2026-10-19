# Task: Coin Combinations II
# Link: https://cses.fi/problemset/task/1636
# Topic: Dynamic Programming / 1D DP (Unordered Combinations / Coin Change)
# Complexity: O(N * X) time, O(X) auxiliary space

import sys

def solve():
    input = sys.stdin.readline
    coins, total_sum = map(int, input().split())
    values = sorted(map(int, input().split()))

    dp = [0] * (total_sum + 1)
    dp[0] = 1

    for j in values:
        for i in range(j, total_sum + 1):
            dp[i] = (dp[i] + dp[i - j]) % (10 ** 9 + 7)

    print(dp[total_sum])


if __name__ == '__main__':
    solve()