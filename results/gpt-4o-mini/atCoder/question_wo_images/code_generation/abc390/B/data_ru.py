N = int(input().strip())
A = list(map(int, input().strip().split()))

if N < 2:
    print("No")
else:
    common_ratio = A[1] / A[0]
    is_geometric = True

    for i in range(1, N - 1):
        if A[i + 1] / A[i] != common_ratio:
            is_geometric = False
            break

    print("Yes" if is_geometric else "No")