from sys import stdin, stdout
from collections import defaultdict, deque

def find_paths_count(n, monsters, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node, parent):
        is_monster = monsters[node - 1]
        for neighbor in tree[node]:
            if neighbor != parent:
                sub_monster = dfs(neighbor, node)
                if sub_monster:
                    is_monster = True
        return is_monster

    return dfs(1, -1)

def process_queries(test_cases):
    results = []
    for n, monsters, edges, queries in test_cases:
        k = find_paths_count(n, monsters, edges)
        results.append(k)
        
        for v in queries:
            monsters[v - 1] = 1 - monsters[v - 1]  # Toggle the monster presence
            k = find_paths_count(n, monsters, edges)
            results.append(k)
            
    return results

def main():
    input = stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    test_cases = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        monsters = list(map(int, data[index].split()))
        index += 1
        edges = []
        
        for _ in range(n - 1):
            u, v = map(int, data[index].split())
            edges.append((u, v))
            index += 1
        
        q = int(data[index])
        index += 1
        queries = []
        
        for _ in range(q):
            v = int(data[index])
            queries.append(v)
            index += 1
        
        test_cases.append((n, monsters, edges, queries))
    
    results = process_queries(test_cases)
    stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()