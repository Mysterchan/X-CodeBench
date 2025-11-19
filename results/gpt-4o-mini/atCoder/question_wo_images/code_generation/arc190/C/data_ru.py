def modinv(a, p):
    return pow(a, p - 2, p)

def precompute_factorials(n, mod):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    return fact

def binomial(n, k, fact, mod):
    if k < 0 or k > n:
        return 0
    return fact[n] * modinv(fact[k], mod) % mod * modinv(fact[n - k], mod) % mod

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
        A.append(list(map(int, data[idx:idx + W])))
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
    
    mod = 998244353
    max_factorial = H + W - 2
    fact = precompute_factorials(max_factorial, mod)
    
    total_paths = binomial(H + W - 2, H - 1, fact, mod)
    
    results = []
    
    for d, a in moves:
        A[sh][sw] = a
        
        f_P = 1
        for i in range(H):
            for j in range(W):
                if i + j < H + W - 1:
                    f_P = f_P * A[i][j] % mod
        
        result = f_P * total_paths % mod
        results.append(result)
        
        if d == 'U':
            sh -= 1
        elif d == 'D':
            sh += 1
        elif d == 'L':
            sw -= 1
        elif d == 'R':
            sw += 1
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()