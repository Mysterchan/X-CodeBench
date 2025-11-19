N = int(input())
A = list(map(int, input().split()))

# For N=2, any two numbers form a geometric progression
if N == 2:
    print("Yes")
    exit()

# Check ratio using fractions to avoid floating point precision issues
# ratio = A[1] / A[0]
# For all i, A[i] * A[0] == A[1] * A[i-1]

first = A[0]
second = A[1]

for i in range(2, N):
    # Cross multiply to avoid float division
    if A[i] * first != A[1] * A[i-1]:
        print("No")
        break
else:
    print("Yes")