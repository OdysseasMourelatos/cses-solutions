"""
Contest: GRCPC 2025
Problem: D. packages
Topic: Binary Search on Answer / Sorting / Greedy
Complexity: O(N * log(N) * log(N)) time, O(N) space
Strategy: Binary search on the answer K (number of packages in [0, N]).
          For a fixed K, each package costs a_i + K * b_i.
          Sort dynamic costs and take the sum of the K cheapest items.
          If sum <= B, we can deliver at least K packages (shift search right);
          otherwise reduce K (shift search left).
"""

import os
import sys

if os.path.exists('input.txt'):
  sys.stdin = open('input.txt', 'r')

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    packages = int(data[0])
    budget = int(data[1])
    costs = []

    for i in range(packages):
        basic_cost = int(data[i+2])
        congestion_coefficient = int(data[i+2+packages])
        costs.append((basic_cost, congestion_coefficient))

    binary_search_on_answer(costs, packages, budget)


def binary_search_on_answer(costs, packages, budget):
    low = 0
    high = packages
    max_packages = 0
    min_cost = 0

    while low <= high:
        packages_wanted = (low + high) // 2

        packages_costs = [a + packages_wanted * b for a, b in costs]

        packages_costs.sort()

        current_cost = sum(packages_costs[:packages_wanted])

        if current_cost <= budget:
            max_packages = packages_wanted
            min_cost = current_cost
            low = packages_wanted + 1
        else:
            high = packages_wanted - 1

    print(max_packages, min_cost)

if __name__ == '__main__':
  solve()