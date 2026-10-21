"""Contest: GRCPC 2025

Problem: C. mansion Topic: Graph / 0-1 BFS / Shortest Path Complexity: O(N + M)
time, O(N + M) space Strategy: Since edge weights are strictly in {0, 1}, we use
a 0-1 BFS with collections.deque. Push weight-0 transitions to the front and
weight-1 transitions to the back to guarantee optimal shortest paths in O(V +
E).
"""

import os
import sys
from collections import deque

if os.path.exists('input.txt'):
  sys.stdin = open('input.txt', 'r')

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)

    rooms = int(next(it))
    doors = int(next(it))

    adj = [[] for _ in range(rooms + 1)]

    for _ in range(doors):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))

    dist = [float('inf') for _ in range(rooms + 1)]
    starting_index = 1
    ending_index = rooms
    bfs(adj, dist, starting_index, ending_index)

def bfs(adj, dist, starting_index, ending_index):
    queue = deque([starting_index])
    dist[starting_index] = 0
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if w == 0:
                    queue.appendleft(v)
                else:
                    queue.append(v)

    print(dist[ending_index] if dist[ending_index] != float('inf') else -1)

if __name__ == '__main__':
  solve()