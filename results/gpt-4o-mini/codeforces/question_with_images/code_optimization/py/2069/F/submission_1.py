from sys import stdin
import sys
from collections import defaultdict

input = stdin.read
sys.setrecursionlimit(10**6)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.component_count = n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            self.component_count -= 1
    
    def get_count(self):
        return self.component_count

def min_edges_to_include(ufA, ufB):
    countA = ufA.get_count()
    countB = ufB.get_count()
    necessary_edges = max(0, countB - countA)
    return necessary_edges

def process_queries(n, queries):
    ufA = UnionFind(n)
    ufB = UnionFind(n)
    edge_set_A = set()
    edge_set_B = set()
    result = []

    for query in queries:
        graph, u, v = query[0], query[1] - 1, query[2] - 1

        if graph == 'A':
            if (u, v) in edge_set_A:
                edge_set_A.remove((u, v))
                ufA.union(u, v)
            else:
                edge_set_A.add((u, v))
                # To roll back the union (as we are effectively adding an edge)
                ufA.union(u, v)
        
        elif graph == 'B':
            if (u, v) in edge_set_B:
                edge_set_B.remove((u, v))
                ufB.union(u, v)
            else:
                edge_set_B.add((u, v))
                # To roll back the union (as we are effectively adding an edge)
                ufB.union(u, v)
        
        result.append(min_edges_to_include(ufA, ufB))

    return result

def main():
    data = input().strip().splitlines()
    n, q = map(int, data[0].split())
    queries = [list(map(str, line.split())) for line in data[1:]]

    results = process_queries(n, queries)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()