def calculate_f(b):
    dark_count = 0
    last_value = -1
    for value in b:
        if value > last_value:
            dark_count += value - last_value
        last_value = value
    return dark_count

def solve(test_cases):
    MOD = 998244353
    results = []
    
    for a in test_cases:
        n = a[0]
        arr = a[1]
        total = 0
        
        for l in range(n):
            max_in_range = 0
            for r in range(l, n):
                max_in_range = max(max_in_range, arr[r])
                total += calculate_f(arr[l:r+1])
                total %= MOD
        
        results.append(total)
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    test_cases = []
    
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        a = list(map(int, data[idx + 1].split()))
        test_cases.append((n, a))
        idx += 2
    
    results = solve(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()