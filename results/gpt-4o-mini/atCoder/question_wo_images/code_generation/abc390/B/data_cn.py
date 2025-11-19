N = int(input())
A = list(map(int, input().split()))

if N < 2:
    print("No")
else:
    r = None
    is_geometric = True

    for i in range(1, N):
        if A[i - 1] == 0:  # to avoid division by zero, not needed since A_i >= 1
            is_geometric = False
            break
        current_r = A[i] / A[i - 1]
        if r is None:
            r = current_r
        elif current_r != r:
            is_geometric = False
            break

    print("Yes" if is_geometric else "No")