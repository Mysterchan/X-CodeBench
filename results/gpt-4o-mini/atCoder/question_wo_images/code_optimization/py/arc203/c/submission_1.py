import sys

MOD = 998244353

MAX_K = 400005
fact = [1] * (MAX_K + 1)
inv_fact = [1] * (MAX_K + 1)
for i in range(2, MAX_K + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[MAX_K] = pow(fact[MAX_K], MOD - 2, MOD)
for i in range(MAX_K - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def nCr_mod(n, r):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    if r > n // 2:
        r = n - r
    
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

def solve():
    H, W, K = map(int, sys.stdin.readline().split())

    total_walls_base = 2 * H * W - H - W

    term_A = term_B = 0
    # Calculate term_A directly
    for j in range(min(H, K + 1)):
        n = total_walls_base - j * W
        if n < K:
            break
        term = nCr_mod(H - 1, j) * nCr_mod(n, K) % MOD
        term_A = (term_A + term) % MOD if j % 2 == 0 else (term_A - term + MOD) % MOD

    # Calculate term_B directly
    for l in range(min(W, K + 1)):
        n = total_walls_base - l * H
        if n < K:
            break
        term = nCr_mod(W - 1, l) * nCr_mod(n, K) % MOD
        term_B = (term_B + term) % MOD if l % 2 == 0 else (term_B - term + MOD) % MOD

    # Final result
    result = (term_A + term_B) % MOD
    print(result)

def main():
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    output = []
    index = 1
    for _ in range(T):
        H = int(data[index])
        W = int(data[index + 1])
        K = int(data[index + 2])
        index += 3
        
        if not (min(H, W) >= 2 and K <= H + W):
            output.append("0")
            continue
        
        total_walls_base = 2 * H * W - H - W
        result = 0

        for j in range(min(H, K) + 1):
            n = total_walls_base - j * W
            if n < K:
                break
            term = nCr_mod(H - 1, j) * nCr_mod(n, K) % MOD
            result = (result + term) % MOD if j % 2 == 0 else (result - term + MOD) % MOD

        for l in range(min(W, K) + 1):
            n = total_walls_base - l * H
            if n < K:
                break
            term = nCr_mod(W - 1, l) * nCr_mod(n, K) % MOD
            result = (result + term) % MOD if l % 2 == 0 else (result - term + MOD) % MOD

        output.append(str(result))
    
    print("\n".join(output))

if __name__ == "__main__":
    main()