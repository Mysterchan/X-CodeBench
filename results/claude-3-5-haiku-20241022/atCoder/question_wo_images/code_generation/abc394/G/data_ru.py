import heapq
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
        
        # BFS with priority queue (Dijkstra)
        # State: (stairs_used, row, col, floor)
        pq = [(0, A, B, Y)]
        visited = {}
        visited[(A, B, Y)] = 0
        
        while pq:
            stairs, r, c, f = heapq.heappop(pq)
            
            if r == C and c == D and f == Z:
                print(stairs)
                break
            
            if (r, c, f) in visited and visited[(r, c, f)] < stairs:
                continue
            
            # Move up/down in the same building
            if f > 1:
                new_state = (r, c, f - 1)
                new_stairs = stairs + 1
                if new_state not in visited or visited[new_state] > new_stairs:
                    visited[new_state] = new_stairs
                    heapq.heappush(pq, (new_stairs, r, c, f - 1))
            
            if f < F[r][c]:
                new_state = (r, c, f + 1)
                new_stairs = stairs + 1
                if new_state not in visited or visited[new_state] > new_stairs:
                    visited[new_state] = new_stairs
                    heapq.heappush(pq, (new_stairs, r, c, f + 1))
            
            # Move to adjacent building via skybridge
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and F[nr][nc] >= f:
                    new_state = (nr, nc, f)
                    if new_state not in visited or visited[new_state] > stairs:
                        visited[new_state] = stairs
                        heapq.heappush(pq, (stairs, nr, nc, f))

solve()