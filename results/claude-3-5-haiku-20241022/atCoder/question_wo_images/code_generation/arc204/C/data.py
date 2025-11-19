def solve():
    N = int(input())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]  # 0-indexed
    
    Q = int(input())
    
    for _ in range(Q):
        A0, A1, A2 = map(int, input().split())
        
        # Find cycles in permutation
        visited = [False] * N
        pairs = []
        
        for i in range(N):
            if not visited[i]:
                j = P[i]
                visited[i] = True
                if j == i:
                    # Self-loop
                    pairs.append((i, i))
                elif not visited[j]:
                    visited[j] = True
                    pairs.append((i, j))
        
        # DP: dp[a0][a1][a2] = max score using exactly a0 zeros, a1 ones, a2 twos
        # Start with all -inf except dp[0][0][0] = 0
        dp = {}
        dp[(0, 0, 0)] = 0
        
        for idx, (i, j) in enumerate(pairs):
            new_dp = {}
            
            for (a0, a1, a2), score in dp.items():
                if i == j:
                    # Single position
                    # Assign 0: MEX(0,0) = 1
                    if a0 + 1 <= A0:
                        key = (a0 + 1, a1, a2)
                        new_dp[key] = max(new_dp.get(key, -float('inf')), score + 1)
                    # Assign 1: MEX(1,1) = 0
                    if a1 + 1 <= A1:
                        key = (a0, a1 + 1, a2)
                        new_dp[key] = max(new_dp.get(key, -float('inf')), score + 0)
                    # Assign 2: MEX(2,2) = 0
                    if a2 + 1 <= A2:
                        key = (a0, a1, a2 + 1)
                        new_dp[key] = max(new_dp.get(key, -float('inf')), score + 0)
                else:
                    # Pair of positions
                    # (0,1): MEX = 2, contribution = 2*2 = 4
                    if a0 + 1 <= A0 and a1 + 1 <= A1:
                        key = (a0 + 1, a1 + 1, a2)
                        new_dp[key] = max(new_dp.get(key, -float('inf')), score + 4)
                    # (0,2): MEX = 1, contribution = 2*1 = 2
                    if a0 + 1 <= A0 and a2 + 1 <= A2:
                        key = (a0 + 1, a1, a2 + 1)
                        new_dp[key] = max(new_dp.get(key, -float('inf')), score + 2)
                    # (1,2): MEX = 0, contribution = 2*0 = 0
                    if a1 + 1 <= A1 and a2 + 1 <= A2:
                        key = (a0, a1 + 1, a2 + 1)
                        new_dp[key] = max(new_dp.get(key, -float('inf')), score + 0)
                    # (0,0): MEX = 1, contribution = 2*1 = 2
                    if a0 + 2 <= A0:
                        key = (a0 + 2, a1, a2)
                        new_dp[key] = max(new_dp.get(key, -float('inf')), score + 2)
                    # (1,1): MEX = 0, contribution = 2*0 = 0
                    if a1 + 2 <= A1:
                        key = (a0, a1 + 2, a2)
                        new_dp[key] = max(new_dp.get(key, -float('inf')), score + 0)
                    # (2,2): MEX = 0, contribution = 2*0 = 0
                    if a2 + 2 <= A2:
                        key = (a0, a1, a2 + 2)
                        new_dp[key] = max(new_dp.get(key, -float('inf')), score + 0)
            
            dp = new_dp
        
        print(dp.get((A0, A1, A2), 0))

solve()