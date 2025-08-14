import heapq

def prims(n, edges, start):
    # Build adjacency list
    adjacency = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adjacency[u].append((v, w))
        adjacency[v].append((u, w))
    
    # Initialize variables
    visited = [False] * (n + 1)
    min_heap = []
    total_weight = 0
    
    # Start with the given node
    visited[start] = True
    for neighbor, weight in adjacency[start]:
        heapq.heappush(min_heap, (weight, neighbor))
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if not visited[u]:
            visited[u] = True
            total_weight += weight
            for neighbor, w in adjacency[u]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (w, neighbor))
    
    return total_weight

# Read input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
start = int(input())

# Compute the MST weight
result = prims(n, edges, start)

# Print the result
print(result)


""" explanation using AI
To solve this problem, we need to find the Minimum Spanning Tree (MST) of a given graph using Prim's algorithm. The MST is a subset of the edges that connects all the vertices together, without any cycles, and with the minimum possible total edge weight. Prim's algorithm starts from an arbitrary node and grows the MST by adding the cheapest edge from the tree to a vertex not yet in the tree.

Approach
Graph Representation: Represent the graph using an adjacency list where each node points to its neighbors along with the edge weights.

Priority Queue (Min-Heap): Use a priority queue to always pick the edge with the smallest weight that connects a node in the MST to a node outside the MST.

Visited Nodes Tracking: Keep track of nodes already included in the MST to avoid cycles.

MST Construction: Start from the given starting node, add all its edges to the priority queue. Then, repeatedly extract the edge with the minimum weight, add the connected node to the MST if not already included, and add its edges to the priority queue. Continue until all nodes are included in the MST. """