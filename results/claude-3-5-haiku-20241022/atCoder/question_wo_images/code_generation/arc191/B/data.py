T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    
    compatible = []
    
    for r in range(N):
        X = r ^ N
        if X > 0 and (X - r) % N == 0:
            compatible.append(X)
    
    compatible.sort()
    
    if len(compatible) >= K:
        print(compatible[K - 1])
    else:
        print(-1)