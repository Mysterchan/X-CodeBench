def count_valid_sequences(N, M):
    MOD = 998244353
    # 2^M
    limit = 1 << M
    # Count of valid sequences
    if N == 1:
        return limit % MOD
    elif N == 2:
        return (limit * (limit - 1) // 2) % MOD
    else:
        # For N >= 3, we can use the formula derived from combinatorial reasoning
        # The number of valid sequences is limit * (limit - 1) * (limit - 2) // 6
        return (limit * (limit - 1) % MOD * (limit - 2) % MOD * pow(6, MOD - 2, MOD)) % MOD

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        result = count_valid_sequences(N, M)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()