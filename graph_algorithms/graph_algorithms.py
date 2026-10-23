"""
Graph Algorithms Cheat Sheet - GRCPC 2025
Περιέχει μόνο τον πυρήνα των αλγορίθμων. Προσαρμόζεται εύκολα σε οποιοδήποτε I/O parsing.
"""
import heapq
from collections import deque


# ==========================================
# 1. 0-1 BFS (Συντομότερα Μονοπάτια με βάρη 0/1)
# ==========================================
def zero_one_bfs(n, adj, start_node):
    dist = [float('inf')] * (n + 1)
    dist[start_node] = 0
    queue = deque([start_node])

    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if w == 0:
                    queue.appendleft(v)
                else:
                    queue.append(v)
    return dist


# ==========================================
# 2. Dijkstra (Συντομότερα Μονοπάτια με θετικά βάρη)
# ==========================================
def dijkstra(n, adj, start_node):
    dist = [float('inf')] * (n + 1)
    pred = [-1] * (n + 1)
    dist[start_node] = 0
    live_dist = [(0, start_node)]

    while live_dist:
        current_weight, u = heapq.heappop(live_dist)

        if current_weight > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                heapq.heappush(live_dist, (dist[v], v))
    return dist, pred


# ==========================================
# 3. Grid BFS & Path Reconstruction (Λαβύρινθοι / Πλέγματα)
# ==========================================
def grid_bfs_path(start_r, start_c, grid, height, width):
    pred = [[None] * width for _ in range(height)]
    queue = deque([(start_r, start_c)])
    pred[start_r][start_c] = 'A'  # Αρχικό σημάδι
    end_pos = (-1, -1)

    while queue:
        r, c = queue.popleft()

        if grid[r][c] == 'B':  # Συνθήκη τερματισμού
            end_pos = (r, c)
            break

        for dr, dc, move in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:
                if pred[nr][nc] is None and grid[nr][nc] != '#':  # '#' = τοίχος
                    pred[nr][nc] = move
                    queue.append((nr, nc))

    # Ανακατασκευή μονοπατιού
    if end_pos != (-1, -1):
        path = []
        i, j = end_pos
        step_back = {'U': (1, 0), 'D': (-1, 0), 'L': (0, 1), 'R': (0, -1)}
        while pred[i][j] != 'A':
            move = pred[i][j]
            path.append(move)
            di, dj = step_back[move]
            i += di
            j += dj
        path.reverse()
        return True, "".join(path)
    return False, ""


# ==========================================
# 4. Topological Sort (Kahn's Algorithm)
# ==========================================
def topological_sort(n, adj, in_degree):
    # Προϋποθέτει 1-based indexing
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    top_order = []

    while queue:
        u = queue.popleft()
        top_order.append(u)

        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(top_order) == n:
        return top_order
    return None  # Υπάρχει κύκλος (Impossible)


# ==========================================
# 5. DSU (Disjoint Set Union / Union-Find)[cite: 3]
# ==========================================
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.num_sets -= 1
            return True
        return False


# ==========================================
# 6. Bipartite Check (Χρωματισμός Διμερούς Γράφου)[cite: 6]
# ==========================================
def is_bipartite(n, adj):
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True