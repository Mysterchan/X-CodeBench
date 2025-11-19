def max_mirages(N, sizes):
    left, right = 0, 0
    pairs = 0
    
    while left < N // 2 and right < N:
        if sizes[left] * 2 <= sizes[right]:
            pairs += 1
            left += 1
        right += 1

    return pairs

# Read input
N = int(input())
sizes = list(map(int, input().split()))

# Get and print the result
result = max_mirages(N, sizes)
print(result)