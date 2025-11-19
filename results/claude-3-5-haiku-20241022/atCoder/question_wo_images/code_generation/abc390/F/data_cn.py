n = int(input())
a = list(map(int, input().split()))

total = 0

for L in range(n):
    seen = set()
    for R in range(L, n):
        seen.add(a[R])
        
        # 计算 f(L, R)
        if len(seen) == 0:
            continue
        
        sorted_vals = sorted(seen)
        segments = 1
        for i in range(1, len(sorted_vals)):
            if sorted_vals[i] - sorted_vals[i-1] > 1:
                segments += 1
        
        total += segments

print(total)