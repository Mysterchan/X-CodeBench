N = int(input())
A = list(map(int, input().split()))

if N == 2:
    print("Yes")
else:
    ratio = A[1] / A[0]
    is_geometric = True
    
    for i in range(2, N):
        if A[i] / A[i - 1] != ratio:
            is_geometric = False
            break
    
    print("Yes" if is_geometric else "No")