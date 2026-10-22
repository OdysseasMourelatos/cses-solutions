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
    max_packages = None
    min_cost = None

    while low <= high:
        packages_wanted = (low + high) // 2

        packages_costs = []
        for c in costs:
            package_cost = c[0] + packages_wanted * c[1]
            packages_costs.append(package_cost)
        packages_costs.sort()

        current_cost = 0
        packages_picked = 0

        for c in packages_costs:
            if c + current_cost <= budget:
                current_cost += c
                packages_picked += 1
                if packages_picked == packages_wanted:
                    break

        if packages_wanted > packages_picked:
            high = packages_wanted - 1
        else:
            max_packages = packages_picked
            min_cost = current_cost
            low = packages_wanted + 1

    print(max_packages, min_cost)

if __name__ == '__main__':
  solve()