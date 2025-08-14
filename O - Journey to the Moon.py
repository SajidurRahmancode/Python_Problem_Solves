import sys
from collections import defaultdict

def journeyToMoon(n, astronaut):
    # Build adjacency list for the graph
    graph = defaultdict(list)
    for u, v in astronaut:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    countries = []
    
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            size = 0
            while stack:
                node = stack.pop()
                size += 1
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            countries.append(size)
    
    total_pairs = n * (n - 1) // 2
    same_country_pairs = 0
    for size in countries:
        same_country_pairs += size * (size - 1) // 2
    
    return total_pairs - same_country_pairs

def main():
    input_lines = sys.stdin.read().split()
    ptr = 0
    n, p = map(int, input_lines[ptr:ptr+2])
    ptr +=2
    astronaut = []
    for _ in range(p):
        u, v = map(int, input_lines[ptr:ptr+2])
        astronaut.append((u, v))
        ptr +=2
    print(journeyToMoon(n, astronaut))

if __name__ == "__main__":
    main()



""" 
To solve this problem, we need to determine the number of valid pairs of astronauts that can be chosen from different countries. The astronauts are grouped into countries based on the given pairs, and we need to calculate the number of ways to select two astronauts from different groups.

Approach
Graph Representation: Represent the astronauts and their pairs as a graph where each node is an astronaut and edges connect astronauts from the same country. This helps in identifying connected components, where each connected component represents a country.

Connected Components: Use a Depth-First Search (DFS) or Union-Find (Disjoint Set Union, DSU) algorithm to find all connected components in the graph. Each connected component will give us the size of each country.

Calculate Valid Pairs: The total number of valid pairs is computed by considering all possible pairs of astronauts and subtracting the pairs that are from the same country. Specifically, if the sizes of the countries are stored in a list sizes, the total pairs can be calculated as:

Total pairs = (total astronauts choose 2) - sum of (each country size choose 2)

Alternatively, we can compute it as the sum of the product of each country size with the sum of sizes of subsequent countries. This approach is more efficient for large numbers of countries. """