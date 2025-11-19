def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(x, y):
    return x // gcd(x, y) * y

def calculate_R(n):
    # R_n is simply `int('1' * n)` which is `10**n - 1 // 9`
    # But we need to use mod efficiently
    return (pow(10, n, 998244353) - 1) * pow(9, 998244353 - 2, 998244353) % 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N + 1]))
    
    lcm_value = 1
    results = []
    
    for i in range(N):
        R_k = calculate_R(A[i])
        lcm_value = lcm(lcm_value, R_k) % 998244353
        results.append(lcm_value)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()