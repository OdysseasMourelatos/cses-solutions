# Task: Coin Combinations I
# Link: https://cses.fi/problemset/task/1635
# Topic: Dynamic Programming / 1D DP (Permutations / Ordered Coin Change)
# Complexity: O(N * X) time, O(X) auxiliary space

import sys


def solve():
    input = sys.stdin.readline
    coins, total_sum = map(int, input().split())
    values = sorted(map(int, input().split()))

    dp = [0] * (total_sum + 1)
    dp[0] = 1

    for i in range(values[0], total_sum + 1):
        s = 0
        for j in values:
            if j > i:
                break
            s += dp[i - j] % (10 ** 9 + 7)
        dp[i] = s % (10 ** 9 + 7)

    print(dp[total_sum])


if __name__ == '__main__':
    solve()