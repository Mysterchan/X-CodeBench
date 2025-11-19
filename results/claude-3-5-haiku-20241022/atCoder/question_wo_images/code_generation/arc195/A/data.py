N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[j] = number of ways to match first j elements of B
dp = [0] * (M + 1)
dp[0] = 1  # empty subsequence

for i in range(N):
    # Process in reverse to avoid using the same element twice
    new_dp = dp[:]
    for j in range(M):
        if A[i] == B[j]:
            new_dp[j + 1] += dp[j]
            # Cap at 2 to avoid overflow and since we only need to know if >= 2
            if new_dp[j + 1] > 2:
                new_dp[j + 1] = 2
    dp = new_dp

if dp[M] >= 2:
    print("Yes")
else:
    print("No")