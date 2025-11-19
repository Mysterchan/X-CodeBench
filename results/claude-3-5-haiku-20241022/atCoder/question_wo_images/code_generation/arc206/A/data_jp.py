def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    sequences = set()
    
    for L in range(N):
        for R in range(L, N):
            # 操作を実行: A[L:R+1] を全て A[L] で置き換える
            result = A[:L] + [A[L]] * (R - L + 1) + A[R+1:]
            sequences.add(tuple(result))
    
    print(len(sequences))

solve()