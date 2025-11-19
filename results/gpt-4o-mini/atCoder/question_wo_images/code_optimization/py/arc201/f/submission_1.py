def cocoa():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        x = y = z = 0
        xy = xyz = 0
        size_results = []
        
        for i in range(N):
            a = int(data[idx])
            b = int(data[idx + 1])
            c = int(data[idx + 2])
            d = int(data[idx + 3])
            e = int(data[idx + 4])
            idx += 5
            
            x += min(a, b, c)
            y += min(b, c, d)
            z += min(c, d, e)
            xy += min(a + d, b, c)
            xyz += min(a + d, b + e, c)
            
            # Calculate the min for all possible divisions
            max_C3C = min(x, xy // 2, xyz // 3, z, y)
            size_results.append(max_C3C)

        results.append(" ".join(map(str, size_results)))
    
    sys.stdout.write("\n".join(results) + "\n")

T = int(input())
for _ in range(T):
    cocoa()