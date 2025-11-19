def count_triples(S):
    n = len(S)
    count = 0
    
    for j in range(1, n - 1):
        if S[j] == 'B':
            # Find i such that S[i] = 'A' and i < j
            for i in range(j):
                if S[i] == 'A' and (j - i) % 2 == 0:
                    k = j + (j - i)
                    if k < n and S[k] == 'C':
                        count += 1
                        
    return count

# Read input
S = input().strip()
# Print the result
print(count_triples(S))