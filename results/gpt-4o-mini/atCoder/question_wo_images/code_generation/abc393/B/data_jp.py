def count_abc_patterns(S):
    count = 0
    n = len(S)
    
    for j in range(1, n - 1):
        if S[j] == 'B':
            # Check for A and C at equal distances from j
            for d in range(1, min(j + 1, n - j)):
                if S[j - d] == 'A' and S[j + d] == 'C':
                    count += 1
                    
    return count

# Read input
S = input().strip()
# Output the result
print(count_abc_patterns(S))