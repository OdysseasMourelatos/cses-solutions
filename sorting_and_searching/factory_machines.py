"""Problem: CSES - Factory Machines

Topic: Binary Search on Answer
Complexity: O(N * log(min_time * T)) time, O(N) space
Strategy: Binary search over the time domain [1, min(k) * T]. For a fixed time X,
          the number of products produced is sum(X // k_i). Find the minimum X
          such that total products >= T.
"""

import os
import sys


if os.path.exists('input.txt'):
  sys.stdin = open('input.txt', 'r')

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)

    machines = int(next(it))
    products = int(next(it))

    min_time = float('inf')
    machine_times = []
    for _ in range(machines):
        time = int(next(it))
        machine_times.append(time)
        min_time = min(min_time, time)

    binary_search_on_answer(machine_times, products, min_time)

def binary_search_on_answer(machine_times, products, min_time):
    low = 0
    high = min_time * products
    answer = None
    while low <= high:
        mid = (low + high) // 2
        products_to_be_produced = 0

        for m in machine_times:
            products_to_be_produced += mid // m
            if products_to_be_produced >= products:
                break

        if products_to_be_produced < products:
            low = mid + 1
        elif products_to_be_produced >= products:
            high = mid - 1
            answer = mid

    print(answer)

if __name__ == '__main__':
  solve()