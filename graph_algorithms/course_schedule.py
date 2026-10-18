# Task: Course Schedule
# Link: https://cses.fi/problemset/task/1679
# Topic: Graph Algorithms / Topological Sort (Kahn's Algorithm) & Cycle Detection
# Complexity: O(V + E) time, O(V + E) auxiliary space

import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    courses, requirements = map(int, input().split())

    required_array = [[] for _ in range(courses)]
    incoming_edges = [0 for _ in range(courses)]
    for _ in range(requirements):
        a, b = map(int, input().split())
        required_array[a-1].append(b)
        incoming_edges[b-1] += 1

    queue = deque()
    for i in range(len(incoming_edges)):
        if incoming_edges[i] == 0:
            queue.append(i)

    topological_order = []
    while queue:
        node = queue.popleft()
        topological_order.append(node+1)
        nodes_affected = required_array[node]
        for n in nodes_affected:
            incoming_edges[n-1] -= 1
            if incoming_edges[n-1] == 0:
                queue.append(n-1)
    if len(topological_order) != courses:
        print("IMPOSSIBLE")
    else:
        for node in topological_order:
            print(node, end=" ")


if __name__ == '__main__':
    solve()
