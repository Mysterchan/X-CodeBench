def main():
    import sys
    input = sys.stdin.read
    N = int(input().strip())
    mod = 998244353

    # Precompute factorials and inverse factorials
    fact = [1] * (N + 1)
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % mod

    # Calculate the contribution of each digit length
    total_sum = 0
    current_length = 1
    while current_length <= N:
        low = 10 ** (current_length - 1)
        high = min(N, 10 ** current_length - 1)
        if low > high:
            break
        count = high - low + 1
        sum_of_numbers = (low + high) * count // 2 % mod
        total_sum = (total_sum + sum_of_numbers * pow(10, current_length - 1, mod) * fact[N - count]) % mod
        current_length += 1

    # Calculate the final result
    result = total_sum * fact[N] % mod
    print(result)

if __name__ == '__main__':
    main()