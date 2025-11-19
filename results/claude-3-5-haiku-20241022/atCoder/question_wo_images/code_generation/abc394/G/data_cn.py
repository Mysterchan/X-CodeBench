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
        
        # BFS with state (row, col, floor, stair_count)
        queue = deque([(A, B, Y, 0)])
        visited = {}
        visited[(A, B, Y)] = 0
        
        result = float('inf')
        
        while queue:
            r, c, floor, stairs = queue.popleft()
            
            if (r, c, floor) in visited and visited[(r, c, floor)] < stairs:
                continue
            
            if r == C and c == D and floor == Z:
                result = min(result, stairs)
                continue
            
            # Try moving via walkway to adjacent blocks
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and F[nr][nc] >= floor:
                    state = (nr, nc, floor)
                    if state not in visited or visited[state] > stairs:
                        visited[state] = stairs
                        queue.append((nr, nc, floor, stairs))
            
            # Try using stairs in current building
            # Go up
            if floor < F[r][c]:
                new_floor = floor + 1
                state = (r, c, new_floor)
                if state not in visited or visited[state] > stairs + 1:
                    visited[state] = stairs + 1
                    queue.append((r, c, new_floor, stairs + 1))
            
            # Go down
            if floor > 1:
                new_floor = floor - 1
                state = (r, c, new_floor)
                if state not in visited or visited[state] > stairs + 1:
                    visited[state] = stairs + 1
                    queue.append((r, c, new_floor, stairs + 1))
        
        print(result)

solve()