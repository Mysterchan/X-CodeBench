N = int(input())
A = list(map(int, input().split()))

is_increasing = all(A[i] < A[i + 1] for i in range(N - 1))

print("Yes" if is_increasing else "No")