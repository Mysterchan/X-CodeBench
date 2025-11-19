from collections import deque

def solve():
    N, X, Y = map(int, input().split())
    S = input().strip()
    T = input().strip()
    
    # Quick check: same character counts
    if S.count('0') != T.count('0'):
        print("No")
        return
    
    if S == T:
        print("Yes")
        return
    
    # BFS to find if T is reachable from S
    visited = {S}
    queue = deque([S])
    
    while queue:
        current = queue.popleft()
        
        if current == T:
            print("Yes")
            return
        
        # Try all possible Operation A
        for i in range(N - X - Y + 1):
            # Check if we can apply Operation A at position i
            if (all(current[i+j] == '0' for j in range(X)) and
                all(current[i+X+j] == '1' for j in range(Y))):
                # Apply Operation A
                new_s = list(current)
                for j in range(Y):
                    new_s[i+j] = '1'
                for j in range(X):
                    new_s[i+Y+j] = '0'
                new_s = ''.join(new_s)
                
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append(new_s)
        
        # Try all possible Operation B
        for i in range(N - X - Y + 1):
            # Check if we can apply Operation B at position i
            if (all(current[i+j] == '1' for j in range(Y)) and
                all(current[i+Y+j] == '0' for j in range(X))):
                # Apply Operation B
                new_s = list(current)
                for j in range(X):
                    new_s[i+j] = '0'
                for j in range(Y):
                    new_s[i+X+j] = '1'
                new_s = ''.join(new_s)
                
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append(new_s)
    
    print("No")

solve()