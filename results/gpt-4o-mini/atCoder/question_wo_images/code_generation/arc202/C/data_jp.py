def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * (y // gcd(x, y))

MOD = 998244353

def main():
    import sys
    from functools import reduce

    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N + 1]))

    current_lcm = 1
    results = []

    for k in range(N):
        R_k = int('1' * A[k])  # R_A[k] is simply 1 repeated A[k] times
        current_lcm = lcm(current_lcm, R_k) % MOD
        results.append(current_lcm)

    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()