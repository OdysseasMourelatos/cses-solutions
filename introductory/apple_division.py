# Task: Apple Division
# Link: https://cses.fi/problemset/task/1623
# Topic: Introductory Problems / Complete Search (Recursion / Subset Sum)
# Complexity: O(2^N) time, O(N) auxiliary space (recursion stack)

import sys

def get_min_diff(index, current_sum):
    if index == n:
        other_sum = total_weight - current_sum
        return abs(current_sum - other_sum)

    take = get_min_diff(index + 1, current_sum + weights[index])
    skip = get_min_diff(index + 1, current_sum)

    return min(take, skip)

n = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
total_weight = sum(weights)
print(get_min_diff(0, 0))

