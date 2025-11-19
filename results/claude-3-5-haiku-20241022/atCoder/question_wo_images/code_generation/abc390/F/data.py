def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    total = 0
    
    for L in range(n):
        distinct = set()
        for R in range(L, n):
            distinct.add(a[R])
            
            # Find f(L, R)
            if len(distinct) == 0:
                continue
            
            sorted_vals = sorted(distinct)
            
            # Count number of contiguous segments
            segments = 1
            for i in range(1, len(sorted_vals)):
                if sorted_vals[i] != sorted_vals[i-1] + 1:
                    segments += 1
            
            total += segments
    
    print(total)

solve()