MOD = 998244353

def modinv(x, mod):
    return pow(x, mod - 2, mod)

def precompute_factorials_and_inverses(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[n] = modinv(fact[n], mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact

def binomial(n, k, fact, inv_fact, mod):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    H = int(data[idx])
    W = int(data[idx + 1])
    idx += 2
    
    A = []
    for h in range(H):
        A.append([int(data[idx + w]) for w in range(W)])
        idx += W
    
    Q = int(data[idx])
    sh = int(data[idx + 1]) - 1
    sw = int(data[idx + 2]) - 1
    idx += 3
    
    moves = []
    for _ in range(Q):
        d = data[idx]
        a = int(data[idx + 1])
        moves.append((d, a))
        idx += 2
    
    fact, inv_fact = precompute_factorials_and_inverses(H + W - 2, MOD)
    
    total_paths = binomial(H + W - 2, H - 1, fact, inv_fact, MOD)
    
    results = []
    
    for d, a in moves:
        if d == 'L':
            sw -= 1
        elif d == 'R':
            sw += 1
        elif d == 'U':
            sh -= 1
        elif d == 'D':
            sh += 1
        
        A[sh][sw] = a
        
        product = 1
        for i in range(H):
            for j in range(W):
                if i + j < H + W - 1:
                    product = product * A[i][j] % MOD
        
        result = product * total_paths % MOD
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()