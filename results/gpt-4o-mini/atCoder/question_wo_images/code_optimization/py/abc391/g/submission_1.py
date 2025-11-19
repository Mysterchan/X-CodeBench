N, M = map(int, input().split())
S = input()
mod = 998244353

# Count occurrences of each character in S
count = [0] * 26
for char in S:
    count[ord(char) - ord('a')] += 1

# Precompute powers of 26
power_of_26 = [1] * (M + 1)
for i in range(1, M + 1):
    power_of_26[i] = (power_of_26[i - 1] * 26) % mod

# Initialize the answer array
ans = [0] * (N + 1)

# Calculate the number of strings with LCS of length k
for k in range(N + 1):
    # Calculate the number of ways to choose k characters from S
    if k > 0:
        ways_to_choose_k = 1
        for i in range(k):
            ways_to_choose_k = (ways_to_choose_k * (count[i] + 1)) % mod
    else:
        ways_to_choose_k = 1

    # Calculate the number of strings of length M with LCS of length k
    ans[k] = (ways_to_choose_k * power_of_26[M - k]) % mod

print(*ans)