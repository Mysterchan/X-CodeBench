T = int(input())
for _ in range(T):
    N = int(input())
    results = []
    
    sum_a, sum_b, sum_c, sum_d, sum_e = 0, 0, 0, 0, 0
    
    for k in range(N):
        a, b, c, d, e = map(int, input().split())
        sum_a += a
        sum_b += b
        sum_c += c
        sum_d += d
        sum_e += e
        
        max_contests = min(sum_a, sum_b // 2, sum_c // 3, sum_d // 2, sum_e)
        results.append(str(max_contests))
    
    print(' '.join(results))