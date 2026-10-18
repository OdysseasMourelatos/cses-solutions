# Task: Message Route
# Link: https://cses.fi/problemset/task/1193
# Topic: Graph Algorithms / BFS Shortest Path & Backtracking on General Graph
# Complexity: O(V + E) time, O(V + E) auxiliary space

import sys
from collections import deque
import bisect

def solve():
    g, total_nodes, total_links = get_graph()
    pred = [-1] * total_nodes
    computer_1 = 1
    computer_n = total_nodes
    value = g.get(computer_1)
    if value is not None:
        bfs(g, computer_1, computer_n, pred)
        if pred[computer_n - 1] == -1:
            print("IMPOSSIBLE")
        else:
            track_path(pred, computer_n)
    else:
        print("IMPOSSIBLE")


def get_graph():
    g = {}
    input = sys.stdin.readline
    total_nodes, total_links = map(int, input().split())
    for _ in range(total_links):
        a, b = map(int, input().split())
        if a not in g:
            g[a] = []
        a_links = g[a]
        if b not in a_links:
            bisect.insort(g[a], b)
        if b not in g:
            g[b] = []
        b_links = g[b]
        if a not in b_links:
            bisect.insort(g[b], a)
    return g, total_nodes, total_links

def bfs(g, starting_node, last_node, pred):
    queue = deque([starting_node])
    stop = False
    while queue and not stop:
        node = queue.popleft()
        for n in g[node]:
            if pred[n-1] == -1 and n != starting_node:
                queue.append(n)
                pred[n-1] = node
                if n == last_node:
                    stop = True
                    break

def track_path(pred, computer_n):
    path = [str(computer_n)]
    i = computer_n
    while pred[i-1] != -1:
        path.append(str(pred[i-1]))
        i = pred[i-1]
    path.reverse()
    print(len(path))
    print(" ".join(path))

if __name__ == '__main__':
    solve()
