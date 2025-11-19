N = int(input())
A = list(map(int, input().split()))

if N == 2:
    print("Yes")
    exit()

# To avoid floating point precision issues, check ratio as fraction
# ratio = A[1]/A[0]
# Check for all i: A[i]*A[0] == A[1]*A[i-1]

a0 = A[0]
a1 = A[1]

for i in range(2, N):
    if A[i] * a0 != A[1] * A[i-1]:
        print("No")
        break
else:
    print("Yes")