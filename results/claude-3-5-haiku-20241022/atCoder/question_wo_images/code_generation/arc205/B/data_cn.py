def solve():
    N, M = map(int, input().split())
    
    for _ in range(M):
        input()
    
    total_edges = N * (N - 1) // 2
    
    if M == 0 and N % 2 == 0:
        print(total_edges - 1)
    else:
        print(total_edges)

solve()