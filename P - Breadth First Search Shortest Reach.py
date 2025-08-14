import sys
from collections import deque

def bfs(n, m, edges, s):
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Initialize distances
    distances = [-1] * (n + 1)
    distances[s] = 0
    q = deque([s])
    
    while q:
        current = q.popleft()
        for neighbor in adj[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 6
                q.append(neighbor)
    
    # Prepare the result, excluding the start node and in order 1 to n
    result = []
    for i in range(1, n + 1):
        if i != s:
            result.append(distances[i])
    return result

if __name__ == "__main__":
    input = sys.stdin.read().split()
    ptr = 0
    q = int(input[ptr])
    ptr += 1
    for _ in range(q):
        n, m = map(int, input[ptr:ptr + 2])
        ptr += 2
        edges = []
        for __ in range(m):
            u, v = map(int, input[ptr:ptr + 2])
            ptr += 2
            edges.append((u, v))
        s = int(input[ptr])
        ptr += 1
        result = bfs(n, m, edges, s)
        print(' '.join(map(str, result)))




""" 
To solve this problem, we need to find the shortest distances from a given start node to all other nodes in an undirected graph where each edge has a weight of 6 units. The solution involves using the Breadth-First Search (BFS) algorithm, which is suitable for finding the shortest path in an unweighted graph (or a graph where all edges have the same weight).
Approach
Graph Representation: Represent the graph using an adjacency list. This allows efficient traversal of each node's neighbors.

BFS Initialization: Start BFS from the given start node. Initialize a distance array where each node's distance is set to -1 (indicating it is initially unreachable) except the start node, which is set to 0.

BFS Execution: Use a queue to process nodes level by level. For each node dequeued, visit all its adjacent nodes. If an adjacent node hasn't been visited (distance is still -1), update its distance to the current node's distance plus 6 and enqueue it.

Result Preparation: After BFS completes, the distance array will contain the shortest distances from the start node to all other nodes. The result should exclude the start node and return distances in increasing order of node numbers (from 1 to n, omitting the start node). 
"""