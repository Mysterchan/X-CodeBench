from collections import deque

def solve():
    H, W = map(int, input().split())
    F = []
    for _ in range(H):
        F.append(list(map(int, input().split())))
    
    Q = int(input())
    
    for _ in range(Q):
        A, B, Y, C, D, Z = map(int, input().split())
        A -= 1
        B -= 1
        C -= 1
        D -= 1
        
        # BFS with state (row, col, floor, stairs_used)
        # We want to minimize stairs_used
        INF = float('inf')
        dist = [[INF] * W for _ in range(H)]
        dist[A][B] = abs(Y - 1) + abs(Y - F[A][B])
        
        pq = deque([(A, B, abs(Y - 1) + abs(Y - F[A][B]))])
        
        while pq:
            r, c, d = pq.popleft()
            
            if d > dist[r][c]:
                continue
            
            # Try moving to adjacent buildings
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    # Calculate minimum stairs needed to reach (nr, nc)
                    # We can use any floor from 1 to min(F[r][c], F[nr][nc])
                    min_f = min(F[r][c], F[nr][nc])
                    
                    # Cost to reach (nr, nc): 
                    # - From current building, go to floor min_f (if possible)
                    # - From (nr, nc), we can be at any floor from 1 to F[nr][nc]
                    
                    # Total cost = cost to reach any floor in [1, min_f] in current building
                    #              + cost from floor f in new building to reach anywhere
                    
                    # The minimum cost to eventually reach (C, D, Z) from (nr, nc)
                    # is the minimum over all reachable floors f in (nr, nc)
                    new_dist = d + abs(min_f - 1) + abs(min_f - F[nr][nc])
                    
                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist
                        pq.append((nr, nc, new_dist))
        
        # Answer is distance to (C, D) plus cost to reach floor Z
        result = dist[C][D] + abs(Z - 1) + abs(Z - F[C][D])
        print(result)

solve()