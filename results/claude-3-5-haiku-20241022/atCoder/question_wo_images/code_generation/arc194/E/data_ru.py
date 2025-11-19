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
        
        current_list = list(current)
        
        # Try Operation A
        for i in range(N - (X + Y) + 1):
            # Check if we can apply Operation A at position i
            if all(current_list[i + j] == '0' for j in range(X)) and \
               all(current_list[i + X + j] == '1' for j in range(Y)):
                # Apply Operation A
                new_list = current_list[:]
                for j in range(Y):
                    new_list[i + j] = '1'
                for j in range(X):
                    new_list[i + Y + j] = '0'
                
                new_state = ''.join(new_list)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)
        
        # Try Operation B
        for i in range(N - (X + Y) + 1):
            # Check if we can apply Operation B at position i
            if all(current_list[i + j] == '1' for j in range(Y)) and \
               all(current_list[i + Y + j] == '0' for j in range(X)):
                # Apply Operation B
                new_list = current_list[:]
                for j in range(X):
                    new_list[i + j] = '0'
                for j in range(Y):
                    new_list[i + X + j] = '1'
                
                new_state = ''.join(new_list)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)
    
    print("No")

solve()