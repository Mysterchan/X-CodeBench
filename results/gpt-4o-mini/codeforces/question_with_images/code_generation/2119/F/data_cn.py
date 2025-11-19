def can_survive_move(n, st, weights, edges):
    from collections import defaultdict, deque
    
    # Build the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # BFS to calculate distances of each node from the start node
    distance = [-1] * (n + 1)
    distance[st] = 0
    queue = deque([st])
    
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if distance[neighbor] == -1:  # Unvisited
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    
    # Now simulate the movement and calculate maximum moves
    max_moves = 0
    current_position = st
    current_life = 1
    
    # We will perform a breadth-first search from the starting point
    queue = deque([(current_position, 0)])  # (node, time)
    
    while queue:
        position, time = queue.popleft()
        
        # Update life at this position
        current_life += weights[position - 1]
        
        if current_life <= 0 or time >= distance[position]:
            continue  # Dead or position is already submerged
        
        max_moves = max(max_moves, time)

        for neighbor in tree[position]:
            if time + 1 <= distance[neighbor]:  # Only consider if neighbor isn't submerged
                queue.append((neighbor, time + 1))
    
    return max_moves

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n, st = map(int, data[idx].split())
        idx += 1
        weights = list(map(int, data[idx].split()))
        idx += 1
        edges = []
        
        for __ in range(n - 1):
            u, v = map(int, data[idx].split())
            edges.append((u, v))
            idx += 1
            
        result = can_survive_move(n, st, weights, edges)
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()