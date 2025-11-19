def count_unique_sequences(N, A):
    unique_values = set(A)
    result = 0
    last_seen = {}
    
    for i in range(N):
        last_seen[A[i]] = i
    
    for i in range(N):
        for value in unique_values:
            if value in last_seen and last_seen[value] >= i:
                result += 1
                break
    
    return result

N = int(input().strip())
A = list(map(int, input().strip().split()))
print(count_unique_sequences(N, A))