import heapq
from collections import defaultdict

def solve():
    H, W = map(int, input().split())
    F = []
    for _ in range(H):
        F.append(list(map(int, input().split())))
    
    Q = int(input())
    
    for _ in range(Q):
        A, B, Y, C, D, Z = map(int, input().split())
        A -= 1  # Convert to 0-indexed
        B -= 1
        C -= 1
        D -= 1
        
        # Dijkstra's algorithm
        # State: (cost, row, col, floor)
        pq = [(0, A, B, Y)]
        visited = {}
        
        while pq:
            cost, r, c, floor = heapq.heappop(pq)
            
            if (r, c, floor) in visited:
                continue
            visited[(r, c, floor)] = cost
            
            if r == C and c == D and floor == Z:
                print(cost)
                break
            
            # Move within the same building to any floor
            for new_floor in range(1, F[r][c] + 1):
                if (r, c, new_floor) not in visited:
                    new_cost = cost + abs(new_floor - floor)
                    heapq.heappush(pq, (new_cost, r, c, new_floor))
            
            # Move to adjacent buildings via walkway at the same floor
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and F[nr][nc] >= floor:
                    if (nr, nc, floor) not in visited:
                        heapq.heappush(pq, (cost, nr, nc, floor))

solve()