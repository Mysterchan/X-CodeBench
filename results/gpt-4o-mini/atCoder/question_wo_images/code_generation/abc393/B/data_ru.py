def count_abc_triplets(S):
    n = len(S)
    count = 0
    
    for j in range(1, n - 1):
        if S[j] == 'B':
            # Calculate i and k based on j
            for d in range(1, min(j + 1, n - j)):
                i = j - d
                k = j + d
                if S[i] == 'A' and S[k] == 'C':
                    count += 1
                    
    return count

# Read input
S = input().strip()
# Print the result
print(count_abc_triplets(S))