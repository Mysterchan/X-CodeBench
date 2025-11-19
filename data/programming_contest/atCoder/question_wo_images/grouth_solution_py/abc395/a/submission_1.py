N = int(input())
A = [int(x) for x in input().split()]
if all(A[i] < A[i + 1] for i in range(N - 1)):
    print("Yes")
else:
    print("No")