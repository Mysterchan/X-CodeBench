def count_ways(N, H, W):
    MOD = 998244353
    if H < N * 2 or W < N * 2:
        return 0
    if H > 3 * N - 1 or W > 3 * N - 1:
        return 0
    
    # Calculate the number of ways to place the tiles
    ways = ((H - N + 1) * (W - N + 1)) % MOD
    return (ways * ways) % MOD

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        N = int(data[index])
        H = int(data[index + 1])
        W = int(data[index + 2])
        index += 3
        
        result = count_ways(N, H, W)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()