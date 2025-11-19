def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def mod_inv(a, mod):
    return pow(a, mod - 2, mod)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N]))
    
    MOD = 998244353
    
    # Calculate the product of all A_i
    product_A = 1
    for a in A:
        product_A = lcm(product_A, a)
    
    # Calculate the total sum of scores
    total_sum = 0
    
    # Generate all possible sequences
    from itertools import product
    
    # Generate all combinations of P and Q for each A_i
    possible_pairs = []
    for a in A:
        pairs = []
        for p in range(1, a + 1):
            if a % p == 0:
                q = a // p
                if gcd(p, q) == 1:
                    pairs.append((p, q))
        possible_pairs.append(pairs)
    
    # Iterate through all combinations of pairs
    for combination in product(*possible_pairs):
        S = [0] * N
        S[0] = combination[0][0]
        S[1] = combination[0][1]
        
        valid = True
        for i in range(1, N - 1):
            S[i + 1] = combination[i][1] * (S[i] // combination[i][0])
            if S[i + 1] <= 0:
                valid = False
                break
        
        if valid and gcd(*S) == 1:
            score = 1
            for s in S:
                score = (score * s) % MOD
            total_sum = (total_sum + score) % MOD
    
    print(total_sum)

if __name__ == "__main__":
    main()