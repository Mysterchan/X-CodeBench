n = int(input())
A = list(map(int, input().split()))

A.sort()
total_score = 0

# Since N is guaranteed to be at least 2, we can directly calculate scores
for i in range(n // 2):
    total_score += A[n - 1 - i] - A[i]

print(total_score)