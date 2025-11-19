N = int(input())
A = list(map(int, input().split()))
print("Yes" if all(A[i] < A[i+1] for i in range(N-1)) else "No")