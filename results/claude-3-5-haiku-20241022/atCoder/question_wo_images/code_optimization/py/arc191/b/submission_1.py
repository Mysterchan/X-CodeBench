t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    # Find the highest bit in n
    m = 1
    while m <= n:
        m *= 2
    
    # Compatible X values are in range [m//2, m)
    # where X ^ n == X % n
    # This happens when X = m//2 + i for i in range(m//2)
    # and (m//2 + i) ^ n == (m//2 + i) % n
    
    # Key insight: X is compatible iff X >= m//2 and X ^ n < n
    # Because X % n = X - n when m//2 <= X < m and X < m
    
    count = 0
    result = -1
    
    # Only check values where X ^ n < n (necessary condition)
    # For X in [m//2, m), X % n = X - n if X >= n, else X
    # We need X ^ n = X % n
    
    for x in range(m // 2, m):
        xor_val = x ^ n
        if xor_val == x % n:
            count += 1
            if count == k:
                result = x
                break
    
    print(result)