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
    total_numbers = mod_exp(2, M, mod)
    
    if N == 1:
        return total_numbers
    
    # Calculate the number of valid sequences
    # The formula derived is total_numbers * (total_numbers - 1)^(N - 1) % mod
    valid_sequences = (total_numbers * mod_exp(total_numbers - 1, N - 1, mod)) % mod
    return valid_sequences

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