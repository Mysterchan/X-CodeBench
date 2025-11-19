def min_max_bench_length(n, m, k):
    # Binary search for the minimum maximum length of bench
    left, right = 1, min(m, k)
    
    while left < right:
        mid = (left + right) // 2
        # Calculate how many benches we can create with max length 'mid'
        benches = 0
        for i in range(n):
            benches += (m // (mid + 1)) * (mid + 1) + min(m % (mid + 1), mid)
        if benches >= k:
            right = mid
        else:
            left = mid + 1
            
    return left

t = int(input())
results = []
for _ in range(t):
    n, m, k = map(int, input().split())
    results.append(min_max_bench_length(n, m, k))

print("\n".join(map(str, results)))