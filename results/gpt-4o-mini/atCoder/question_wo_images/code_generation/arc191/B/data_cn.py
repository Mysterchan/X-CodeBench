def find_kth_compatible(N, K):
    compatible_numbers = []
    x = 1
    while len(compatible_numbers) < K:
        if (x ^ N) == (x % N):
            compatible_numbers.append(x)
        x += 1
    return compatible_numbers[K - 1] if len(compatible_numbers) >= K else -1

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N, K = map(int, data[i].split())
        result = find_kth_compatible(N, K)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()