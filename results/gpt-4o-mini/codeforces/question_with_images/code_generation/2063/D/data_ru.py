def max_triangle_area(a, b):
    return (max(a) - min(a)) * 2

def solve(test_cases):
    results = []
    for n, m, a, b in test_cases:
        if n < 1 or m < 1:
            results.append((0, []))
            continue
        
        k_max = min(n, m)
        areas = []
        
        for k in range(1, k_max + 1):
            area = k * max_triangle_area(a[-k:], b[-k:])
            areas.append(area)
        
        results.append((k_max, areas))
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    test_cases = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        a = list(map(int, data[index + 1].split()))
        b = list(map(int, data[index + 2].split()))
        test_cases.append((n, m, a, b))
        index += 3
    
    results = solve(test_cases)
    
    output = []
    for k_max, areas in results:
        output.append(str(k_max))
        if k_max > 0:
            output.append(" ".join(map(str, areas)))
    
    print("\n".join(output))

if __name__ == "__main__":
    main()