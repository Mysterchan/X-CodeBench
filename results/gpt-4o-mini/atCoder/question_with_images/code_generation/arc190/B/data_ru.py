def mod_inv(x, mod):
    return pow(x, mod - 2, mod)

def count_ways(N, a, b, k):
    mod = 998244353

    if k > min(N - a + 1, N - b + 1) and k > min(a, b):
        return 0

    left_choices = (b - 1) + (N - b)
    up_choices = (a - 1) + (N - a)

    total_ways = (left_choices + 1) * (up_choices + 1) % mod
    return total_ways

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    a = int(data[1])
    b = int(data[2])
    Q = int(data[3])
    k_list = list(map(int, data[4:4 + Q]))
    
    results = []
    for k in k_list:
        results.append(count_ways(N, a, b, k))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()