def count_mirrored_mochis(N, A):
    count = 0
    j = 0

    for i in range(N):
        while j < N and A[j] <= 2 * A[i]:
            j += 1
        count += j - i - 1  # subtract 1 to not count A[i] itself

    return count

# Read input
N = int(input())
A = list(map(int, input().split()))

# Get the result
result = count_mirrored_mochis(N, A)

# Output the result
print(result)