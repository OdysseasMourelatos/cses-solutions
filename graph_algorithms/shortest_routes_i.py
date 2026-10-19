# Task: Shortest Routes I
# Link: https://cses.fi/problemset/task/1671
# Topic: Graph Algorithms / Dijkstra's Algorithm (Single-Source Shortest Path)
# Complexity: O((V + E) log V) time, O(V + E) auxiliary space

import sys
import heapq

def solve():
    g, total_nodes, total_links = get_graph()
    pred = [-1] * total_nodes
    dist = [-1] * total_nodes
    starting_node = 1
    dijkstra(g, starting_node, dist, pred)

def get_graph():
    input = sys.stdin.readline
    total_nodes, total_links = map(int, input().split())
    graph = [[] for _ in range(total_nodes)]
    for _ in range(total_links):
        a, b, weight = list(map(int, sys.stdin.readline().split()))
        graph[a-1].append((b, weight))
    return graph, total_nodes, total_links

def dijkstra(g, starting_node, dist, pred):
    live_dist = [(0, starting_node)]
    heapq.heapify(live_dist)
    dist[starting_node-1] = 0

    while len(live_dist) != 0:
        current_weight, node = heapq.heappop(live_dist)
        node = node - 1

        if current_weight > dist[node]:
            continue

        for neighbor, weight in g[node]:
            if dist[neighbor-1] == -1 or dist[node] + weight < dist[neighbor-1]:
                dist[neighbor-1] = dist[node] + weight
                pred[neighbor-1] = node
                heapq.heappush(live_dist, (dist[neighbor - 1], neighbor))

    print(*dist)

if __name__ == '__main__':
    solve()
