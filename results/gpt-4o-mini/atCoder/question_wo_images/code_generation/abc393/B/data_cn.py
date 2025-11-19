def count_triplets(S):
    count = 0
    n = len(S)
    
    for j in range(1, n - 1):
        if S[j] == 'B':
            for i in range(j):
                if S[i] == 'A' and (j - i) % 2 == 0:
                    k = j + (j - i)
                    if k < n and S[k] == 'C':
                        count += 1
    return count

S = input().strip()
print(count_triplets(S))