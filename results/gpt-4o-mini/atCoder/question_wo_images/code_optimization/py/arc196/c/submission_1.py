M = 998244353

# Function to compute factorial and modular inverse factorial
def preprocess_factorials(n):
    fact = [1] * (2 * n + 1)
    inv_fact = [1] * (2 * n + 1)
    for i in range(2, 2 * n + 1):
        fact[i] = fact[i - 1] * i % M
    inv_fact[2 * n] = pow(fact[2 * n], M - 2, M)
    for i in range(2 * n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % M
    return fact, inv_fact

def count_ways_to_pair(n, s):
    count_w = count_b = 0
    for char in s:
        if char == 'W':
            count_w += 1
        else:
            count_b += 1

    if count_w != count_b:
        return 0

    fact, inv_fact = preprocess_factorials(n)

    dp = [0] * (n + 1)
    dp[0] = 1  # 1 way to pair zero vertices

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * (count_w - (i - 1)) % M

    result = dp[n] * fact[n] % M
    return result

n = int(input())
s = input().strip()
print(count_ways_to_pair(n, s))