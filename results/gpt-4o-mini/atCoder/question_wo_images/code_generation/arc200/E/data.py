def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def count_sequences(N, M):
    mod = 998244353
    if N == 1:
        return mod_exp(2, M, mod)
    
    # Total valid numbers in the range [0, 2^M)
    total_numbers = mod_exp(2, M, mod)
    
    # Calculate the number of valid sequences
    # The number of ways to choose 1 number is total_numbers
    # The number of ways to choose 2 numbers such that their popcount is <= 2
    # For each number, we can choose 0, 1, or 2 bits to differ from it.
    
    # Count of valid pairs (A_i, A_j) where popcount(A_i XOR A_j) <= 2
    valid_pairs = total_numbers * (total_numbers - 1) // 2
    
    # Each number can be chosen independently
    # The total number of valid sequences is:
    # total_numbers * (valid_pairs + total_numbers)^(N-1)
    
    # We need to calculate (valid_pairs + total_numbers)^(N-1) % mod
    total_ways = (valid_pairs + total_numbers) % mod
    total_ways = mod_exp(total_ways, N - 1, mod)
    
    # The final answer is total_numbers * total_ways % mod
    return (total_numbers * total_ways) % mod

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
        results.append(count_sequences(N, M))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()