"""
Dynamic Programming Cheat Sheet - GRCPC 2025
"""
import bisect


# ==========================================
# 1. Knapsack & Coin Change Variations (1D Array)
# ==========================================
def dp_knapsack_variations(items, target_capacity):
    # Παράδειγμα 1: 0-1 Knapsack (Book Shop) - Κάθε item 1 φορά
    dp_01 = [0] * (target_capacity + 1)
    for weight, value in items:
        for w in range(target_capacity, weight - 1, -1):  # ΑΝΑΠΟΔΑ
            dp_01[w] = max(dp_01[w], dp_01[w - weight] + value)

    # Παράδειγμα 2: Coin Combinations II (ΔΕΝ μετράει η σειρά π.χ. {1,2} == {2,1})
    dp_comb = [0] * (target_capacity + 1)
    dp_comb[0] = 1
    for coin in items:  # COINS ΕΞΩ
        for i in range(coin, target_capacity + 1):  # ΚΑΝΟΝΙΚΑ
            dp_comb[i] = (dp_comb[i] + dp_comb[i - coin]) % 1000000007

    # Παράδειγμα 3: Coin Combinations I (ΜΕΤΡΑΕΙ η σειρά π.χ. {1,2} != {2,1})
    dp_perm = [0] * (target_capacity + 1)
    dp_perm[0] = 1
    for i in range(1, target_capacity + 1):  # CAPACITY ΕΞΩ
        for coin in items:  # COINS ΜΕΣΑ
            if i >= coin:
                dp_perm[i] = (dp_perm[i] + dp_perm[i - coin]) % 1000000007


# ==========================================
# 2. Longest Increasing Subsequence O(N log N)
# ==========================================
def longest_increasing_subsequence(arr):
    # Ο(N log N) αντί για O(N^2)
    sub = []
    for val in arr:
        pos = bisect.bisect_left(sub, val)
        if pos == len(sub):
            sub.append(val)
        else:
            sub[pos] = val
    return len(sub)


# ==========================================
# 3. 2D DP (Longest Common Subsequence)
# ==========================================
def longest_common_subsequence(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]