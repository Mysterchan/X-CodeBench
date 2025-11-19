t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    
    compatible_numbers = []
    
    # Calculate compatible numbers
    for x in range(n, n + k + n):  # Check only the first 2*K numbers above N, it would be sufficient
        if (x ^ n) == (x % n):
            compatible_numbers.append(x)
            if len(compatible_numbers) == k:
                break
    
    if len(compatible_numbers) >= k:
        results.append(compatible_numbers[k - 1])
    else:
        results.append(-1)

print('\n'.join(map(str, results)))