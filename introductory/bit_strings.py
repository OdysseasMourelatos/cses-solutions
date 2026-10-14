# Task: Bit Strings
# Link: https://cses.fi/problemset/task/1617
# Topic: Introductory Problems / Combinatorics & Modular Arithmetic
# Complexity: O(log N) time, O(1) space

import sys

def solve():
    n = int(sys.stdin.readline())
    MOD = 10 ** 9 + 7
    ans = pow(2, n, MOD)
    print(ans)


if __name__ == '__main__':
    solve()