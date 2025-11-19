def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1  # 0-indexed
        
        mochis = A[L:R]
        n = len(mochis)
        
        # Greedy approach: try to pair smallest with largest possible
        used = [False] * n
        count = 0
        
        for i in range(n):
            if used[i]:
                continue
            # Try to find the largest mochi that can be placed on top of mochi i
            for j in range(n - 1, i, -1):
                if not used[j] and mochis[i] * 2 >= mochis[j]:
                    used[i] = True
                    used[j] = True
                    count += 1
                    break
        
        print(count)

solve()