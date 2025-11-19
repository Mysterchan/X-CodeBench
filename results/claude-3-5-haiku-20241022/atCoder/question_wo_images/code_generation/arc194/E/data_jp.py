from collections import deque

def solve():
    N, X, Y = map(int, input().split())
    S = input().strip()
    T = input().strip()
    
    if S == T:
        print("Yes")
        return
    
    # BFS to check if S can be transformed to T
    visited = {S}
    queue = deque([S])
    
    while queue:
        current = queue.popleft()
        
        if current == T:
            print("Yes")
            return
        
        # Try operation A: X zeros followed by Y ones -> Y ones followed by X zeros
        for i in range(N - (X + Y) + 1):
            # Check if positions i to i+X-1 are all 0 and i+X to i+X+Y-1 are all 1
            if all(current[j] == '0' for j in range(i, i + X)) and \
               all(current[j] == '1' for j in range(i + X, i + X + Y)):
                # Apply operation A
                new_s = list(current)
                for j in range(i, i + Y):
                    new_s[j] = '1'
                for j in range(i + Y, i + Y + X):
                    new_s[j] = '0'
                new_s = ''.join(new_s)
                
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append(new_s)
        
        # Try operation B: Y ones followed by X zeros -> X zeros followed by Y ones
        for i in range(N - (X + Y) + 1):
            # Check if positions i to i+Y-1 are all 1 and i+Y to i+Y+X-1 are all 0
            if all(current[j] == '1' for j in range(i, i + Y)) and \
               all(current[j] == '0' for j in range(i + Y, i + Y + X)):
                # Apply operation B
                new_s = list(current)
                for j in range(i, i + X):
                    new_s[j] = '0'
                for j in range(i + X, i + X + Y):
                    new_s[j] = '1'
                new_s = ''.join(new_s)
                
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append(new_s)
    
    print("No")

solve()