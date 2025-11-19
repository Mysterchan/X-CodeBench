def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def count_sequences(N, M):
    MOD = 998244353
    if N == 1:
        return mod_exp(2, M, MOD)
    
    # Total number of valid sequences
    total = mod_exp(2, M, MOD)
    
    # Calculate the number of ways to choose 2 elements from N
    # C(N, 2) = N * (N - 1) // 2
    ways_to_choose_2 = (N * (N - 1) // 2) % MOD
    
    # Each pair can differ in at most 2 bits
    # There are 3 cases for each pair (same, differ in 1 bit, differ in 2 bits)
    # For each pair, we can choose 1 of the 3 configurations
    valid_pairs = (total * 3) % MOD
    
    # Total valid sequences
    result = (total * mod_exp(valid_pairs, ways_to_choose_2, MOD)) % MOD
    return result

import sys
input = sys.stdin.read

def main():
    data = input().split()
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        results.append(count_sequences(N, M))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()