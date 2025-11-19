def minimum_length(t, cases):
    results = []
    for n, m, k in cases:
        # Binary search for the minimum maximum group length
        low, high = 1, max(1, k // n + (k % n > 0))
        while low < high:
            mid = (low + high) // 2
            # Can we fit k tables with max group length of mid?
            if mid * n >= k + (mid - 1) * (n - k // mid):
                high = mid
            else:
                low = mid + 1
        results.append(low)
    
    return results

# Input processing
t = int(input())
cases = [tuple(map(int, input().split())) for _ in range(t)]

# Calculate results
results = minimum_length(t, cases)

# Output results
for result in results:
    print(result)