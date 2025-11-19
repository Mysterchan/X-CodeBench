def count_lcs(S, M, k):
    from itertools import product
    
    MOD = 998244353
    N = len(S)
    total_strings = 26 ** M
    
    # Count the number of strings of length M with LCS of length k
    def lcs_count(k):
        if k > N:
            return 0
        if k == 0:
            # Count strings with no common characters
            return (26 - len(set(S))) ** M
        if k == N:
            # Count strings that are exactly S
            return 1 if M >= N else 0
        
        # Count strings with exactly k common characters
        count = 0
        for chars in product('abcdefghijklmnopqrstuvwxyz', repeat=M):
            lcs_length = 0
            for char in chars:
                if char in S:
                    lcs_length += 1
            if lcs_length == k:
                count += 1
                count %= MOD
        return count
    
    results = [lcs_count(k) for k in range(N + 1)]
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
S = data[2]

# Get results
results = count_lcs(S, M, N)

# Print results
print(' '.join(map(str, results)))