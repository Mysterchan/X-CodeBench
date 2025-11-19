from collections import deque

def solve():
    N, X, Y = map(int, input().split())
    S = input().strip()
    T = input().strip()
    
    if S == T:
        print("Yes")
        return
    
    # BFS to find if we can transform S to T
    visited = {S}
    queue = deque([S])
    
    while queue:
        current = queue.popleft()
        
        if current == T:
            print("Yes")
            return
        
        # Try operation A: X consecutive 0s followed by Y consecutive 1s
        # Change first Y positions to 1, next X positions to 0
        for i in range(N - X - Y + 1):
            # Check if we can apply operation A at position i
            can_apply_a = True
            for j in range(X):
                if current[i + j] != '0':
                    can_apply_a = False
                    break
            if can_apply_a:
                for j in range(Y):
                    if current[i + X + j] != '1':
                        can_apply_a = False
                        break
            
            if can_apply_a:
                # Apply operation A
                new_s = list(current)
                for j in range(Y):
                    new_s[i + j] = '1'
                for j in range(X):
                    new_s[i + Y + j] = '0'
                new_s = ''.join(new_s)
                
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append(new_s)
        
        # Try operation B: Y consecutive 1s followed by X consecutive 0s
        # Change first X positions to 0, next Y positions to 1
        for i in range(N - X - Y + 1):
            # Check if we can apply operation B at position i
            can_apply_b = True
            for j in range(Y):
                if current[i + j] != '1':
                    can_apply_b = False
                    break
            if can_apply_b:
                for j in range(X):
                    if current[i + Y + j] != '0':
                        can_apply_b = False
                        break
            
            if can_apply_b:
                # Apply operation B
                new_s = list(current)
                for j in range(X):
                    new_s[i + j] = '0'
                for j in range(Y):
                    new_s[i + X + j] = '1'
                new_s = ''.join(new_s)
                
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append(new_s)
    
    print("No")

solve()