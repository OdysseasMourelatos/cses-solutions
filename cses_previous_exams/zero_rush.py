"""
Contest: GRCPC 2025
Problem: A. zerorush
Topic: Basic Math / Parity / Ad-hoc
Complexity: O(N) time, O(N) space (O(1) auxiliary)
Strategy: Check if any number is even (reachable by steps of 2).
          Minimize |x| / 2 across all even numbers, or return -1 if none exists.
"""

import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    weights = list(map(int, sys.stdin.readline().split()))
    min_difference = float('inf')
    for w in weights:
        abs_w = abs(w)
        if abs_w % 2 == 0:
            min_difference = min(min_difference, abs_w)

    print(-1 if min_difference == float('inf') else min_difference // 2)

if __name__ == '__main__':
    solve()
