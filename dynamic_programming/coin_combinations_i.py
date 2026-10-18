# Task: Coin Combinations I
# Link: https://cses.fi/problemset/task/1635
# Topic: Dynamic Programming / 1D DP (Permutations / Ordered Coin Change)
# Complexity: O(N * X) time, O(X) auxiliary space

import sys

def solve():
    input = sys.stdin.readline
    coins, sum = map(int, input().split())
    values = list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(sum + 1)]
    dp[0] = 1
    min_value = min(values)
    for i in range(min_value, sum + 1):
        for j in values:
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % (10 ** 9 + 7)

    print(dp[sum])

if __name__ == '__main__':
    solve()