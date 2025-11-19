def max_moves_in_tree(test_cases):
    results = []
    for n, start, weights, edges in test_cases:
        from collections import defaultdict, deque
        
        # Construct the tree from edges
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # BFS to determine the maximum distances and calculate moves
        def bfs(start):
            queue = deque([start])
            visited = {start: 0}  # node: distance from start
            distances = []
            
            while queue:
                node = queue.popleft()
                curr_dist = visited[node]
                distances.append((curr_dist, node))
                
                for neighbor in tree[node]:
                    if neighbor not in visited:
                        visited[neighbor] = curr_dist + 1
                        queue.append(neighbor)
            
            return distances
        
        distances = bfs(start)
        # Sort by distance from root
        distances.sort()
        
        max_moves = 0
        lives = 1  # Starts with 1 life
        time = 0
        
        for dist, node in distances:
            if dist > time:  # Lave has reached or passed, die
                break
            lives += weights[node - 1]  # Update lives
            if lives <= 0:  # If lives become 0, die
                break
            max_moves += 1
            time += 1  # Move to the next time frame
        
        results.append(max_moves)
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split('\n')
index = 0
T = int(data[index])
index += 1
test_cases = []

for _ in range(T):
    n, st = map(int, data[index].split())
    index += 1
    weights = list(map(int, data[index].split()))
    index += 1
    edges = []
    for _ in range(n - 1):
        u, v = map(int, data[index].split())
        edges.append((u, v))
        index += 1
    
    test_cases.append((n, st, weights, edges))

# Get results
results = max_moves_in_tree(test_cases)

# Output results
sys.stdout.write('\n'.join(map(str, results)) + '\n')