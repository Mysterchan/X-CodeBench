def count_good_triplets(N, S):
    S_set = set(S)
    count = 0
    
    for b in S:
        for a in range(1, b):
            c = 2 * b - a
            if c > b and c in S_set:
                count += 1
                
    return count

# Read input
N = int(input())
S = list(map(int, input().split()))

# Get the result and print it
result = count_good_triplets(N, S)
print(result)