def max_triangle_area(a, b):
    return (max(a) - min(a)) * (max(b) - min(b))

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        a = list(map(int, data[index].split()))
        index += 1
        b = list(map(int, data[index].split()))
        index += 1
        
        k_max = min(n, m)
        results.append(str(k_max))
        
        if k_max > 0:
            f = []
            for k in range(1, k_max + 1):
                area = max_triangle_area(a[-k:], b[-k:])
                f.append(str(area))
            results.append(" ".join(f))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()