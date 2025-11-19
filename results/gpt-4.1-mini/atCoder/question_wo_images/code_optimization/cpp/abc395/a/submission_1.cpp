n = int(input())
A = list(map(int, input().split()))
print("Yes" if all(A[i] < A[i+1] for i in range(n-1)) else "No")