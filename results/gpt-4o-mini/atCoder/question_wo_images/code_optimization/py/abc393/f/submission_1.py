def solve():
    import sys
    from bisect import bisect_left

    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    a = list(map(int, data[2:n+2]))
    
    queries = []
    for i in range(q):
        r = int(data[n + 2 + 2 * i])
        x = int(data[n + 3 + 2 * i])
        queries.append((r, x))
    
    results = []
    
    for r, x in queries:
        # Create a filtered list of elements from A[0] to A[r-1] that are <= x
        filtered = [a[i] for i in range(r) if a[i] <= x]
        
        if not filtered:
            results.append(0)
            continue
        
        # Find the length of the longest increasing subsequence
        dp = []
        for val in filtered:
            pos = bisect_left(dp, val)
            if pos == len(dp):
                dp.append(val)
            else:
                dp[pos] = val
        
        results.append(len(dp))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

solve()