def min_length(A):
    n = len(A)
    if n == 0:
        return 0
    
    # 連続する同じ値のグループ数を数える
    groups = 1
    for i in range(1, n):
        if A[i] != A[i-1]:
            groups += 1
    
    # グループ数が答え
    return groups

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    i = int(input())
    A[i-1] = 1 - A[i-1]
    print(min_length(A))