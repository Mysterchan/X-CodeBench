from collections import deque

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    # すでに全て1ならYes
    if all(a == 1 for a in A):
        print("Yes")
        return
    
    # BFS で到達可能な状態を探索
    initial = tuple(A)
    queue = deque([initial])
    visited = {initial}
    
    while queue:
        state = queue.popleft()
        
        # 全て1ならYes
        if all(s == 1 for s in state):
            print("Yes")
            return
        
        # 各位置で操作を試す
        for i in range(N):
            # ARC パターン (i, i+1, i+2)
            # S_i=A, S_{i+1}=R, S_{i+2}=C で A_i, A_{i+1} を 1 に
            new_state = list(state)
            new_state[i] = 1
            new_state[(i + 1) % N] = 1
            new_tuple = tuple(new_state)
            if new_tuple not in visited:
                visited.add(new_tuple)
                queue.append(new_tuple)
            
            # CRA パターン (i, i+1, i+2)
            # S_{i+2}=A, S_{i+1}=R, S_i=C で A_i, A_{i+1} を 1 に
            new_state = list(state)
            new_state[i] = 1
            new_state[(i + 1) % N] = 1
            new_tuple = tuple(new_state)
            if new_tuple not in visited:
                visited.add(new_tuple)
                queue.append(new_tuple)
    
    print("No")

solve()