# Task: Weird Algorithm
# Link: https://cses.fi/problemset/task/1068
# Topic: Introductory Problems (Simulation / Collatz Conjecture)
# Complexity: Time depends on sequence length (approx. O(steps)), O(steps) auxiliary space

import sys

def solve():
    x = sys.stdin.readline()
    x = int(x)
    values = [x]
    while x != 1:
        if x % 2 == 0:
            x = int(x / 2)
        else:
            x = x * 3 + 1
        values.append(x)
    for value in values:
        print(value, end = " ")

if __name__ == '__main__':
    solve()