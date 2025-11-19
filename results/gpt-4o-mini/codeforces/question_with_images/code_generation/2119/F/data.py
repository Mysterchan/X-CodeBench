def max_moves(n, st, weights, edges):
    from collections import defaultdict, deque
    
    # Build the tree from the edge list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # BFS to calculate distances from the root
    distances = [-1] * (n + 1)
    distances[1] = 0
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        for neighbor in tree[current]:
            if distances[neighbor] == -1:  # not visited
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    # Simulate the moves
    current_pos = st
    S = 1
    moves = 0
    time = 0
    
    # This is the set of vertices we can reach without being flooded
    reachable_set = set()
    
    while True:
        # Increment life value by weight of current position
        S += weights[current_pos - 1]
        
        if S <= 0 or distances[current_pos] <= time:
            break  # Die condition
        
        # Mark the current position as reachable
        reachable_set.add(current_pos)
        
        # Prepare to move to an adjacent vertex
        time += 1
        next_pos = None
        
        # Try to find a valid position to move to
        for neighbor in tree[current_pos]:
            if neighbor not in reachable_set:
                next_pos = neighbor
                break
        
        if next_pos is None:
            break  # No valid move available
        
        current_pos = next_pos
        moves += 1

    return moves

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    output = []
    
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
        
        result = max_moves(n, st, weights, edges)
        output.append(str(result))
    
    print("\n".join(output))

if __name__ == "__main__":
    main()