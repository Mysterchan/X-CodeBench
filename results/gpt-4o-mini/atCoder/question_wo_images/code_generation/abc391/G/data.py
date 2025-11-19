def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def count_lcs_strings(N, M, S):
    MOD = 998244353
    total_strings = mod_exp(26, M, MOD)
    
    # Count frequency of each character in S
    freq = [0] * 26
    for char in S:
        freq[ord(char) - ord('a')] += 1
    
    # dp[k] will store the number of strings with LCS of length k
    dp = [0] * (N + 1)
    dp[0] = total_strings  # All strings have LCS of length 0
    
    for k in range(1, N + 1):
        # Calculate the number of strings with LCS of length k
        # We need to consider the contribution of each character in S
        # to the LCS of length k
        dp[k] = 0
        for i in range(26):
            if freq[i] > 0:
                # If we take this character, we can form strings of length M-k
                # with the remaining characters
                dp[k] += (freq[i] * mod_exp(26, M - k, MOD)) % MOD
                dp[k] %= MOD
        
        # We need to subtract the cases where we have LCS longer than k
        if k > 1:
            dp[k] = (dp[k] - dp[k - 1] + MOD) % MOD
    
    return dp

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    S = data[2]
    
    results = count_lcs_strings(N, M, S)
    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()