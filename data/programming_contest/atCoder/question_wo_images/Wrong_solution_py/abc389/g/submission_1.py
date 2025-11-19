def comb(n, k, mod):

    num = 1
    for i in range(k):
        num = (num * (n - i)) % mod
    den = 1
    for i in range(1, k + 1):
        den = (den * i) % mod
    return (num * pow(den, mod - 2, mod)) % mod

def pow_mod(base, exponent, mod):

    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent //= 2
        base = (base * base) % mod
    return result

N, P = map(int, input().split())
result = []
for M in range(N - 1, N * (N - 1) // 2 + 1):
    total = 0
    for k in range(1, N // 2 + 1):

        ways_to_choose_k = comb(N - 1, k, P)

        ways_to_choose_edges = comb((N - k - 1) * (N - k - 2) // 2, M - k * (k - 1) // 2, P)

        ways_to_choose_k_edges = comb(k * (k - 1) // 2, k * (k - 1) // 2, P)

        total += (ways_to_choose_k * ways_to_choose_edges * ways_to_choose_k_edges) % P
    result.append(total % P)
print(*result)