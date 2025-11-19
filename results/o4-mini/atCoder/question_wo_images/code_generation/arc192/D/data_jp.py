def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * (b // gcd(a, b))

def calculate_good_sequences(N, A):
    MOD = 998244353
    # dp[i][g] will store the sum of scores for sequences of length i with gcd g
    dp = [{} for _ in range(N + 1)]
    dp[1][1] = 1  # Base case: one way to have a sequence of length 1 with gcd 1

    for i in range(1, N):
        a = A[i - 1]
        for g in dp[i].keys():
            # We need to find all pairs (P, Q) such that f(P/Q) = a
            for P in range(1, a + 1):
                if a % P == 0:
                    Q = a // P
                    new_g = gcd(g, P * Q)
                    if new_g not in dp[i + 1]:
                        dp[i + 1][new_g] = 0
                    dp[i + 1][new_g] = (dp[i + 1][new_g] + dp[i][g] * (P * Q)) % MOD

    # Sum all scores for sequences of length N with gcd 1
    return dp[N].get(1, 0)

# Input reading
N = int(input())
A = list(map(int, input().split()))

# Calculate and print the result
result = calculate_good_sequences(N, A)
print(result)