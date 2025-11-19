N = int(input())
A = list(map(int, input().split()))

if N == 2:
    print("Yes")
    exit()

# Check if the sequence is geometric
# Handle zero division carefully
# The ratio can be a fraction, so compare cross multiplication to avoid float precision issues

# If A[0] == 0, then for geometric sequence all must be zero
if A[0] == 0:
    if all(x == 0 for x in A):
        print("Yes")
    else:
        print("No")
    exit()

# Calculate ratio as a fraction: r = A[1]/A[0]
# Check for all i: A[i]*A[0] == A[i-1]*A[1]
r_num = A[1]
r_den = A[0]

for i in range(2, N):
    if A[i] * r_den != A[i-1] * r_num:
        print("No")
        break
else:
    print("Yes")