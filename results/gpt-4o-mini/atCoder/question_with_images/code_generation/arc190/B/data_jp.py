MOD = 998244353

def count_L_shapes(N, a, b, k):
    max_k = min(a, b, N - a + 1, N - b + 1)
    if k > max_k:
        return 0
    return (N - k + 1) * (N - k + 1) % MOD

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    a = int(data[1])
    b = int(data[2])
    Q = int(data[3])
    queries = list(map(int, data[4:4 + Q]))

    results = [count_L_shapes(N, a, b, k) for k in queries]
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()