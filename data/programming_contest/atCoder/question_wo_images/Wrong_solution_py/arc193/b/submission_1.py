MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    s = data[1]

    K = s.count('1')

    part1 = (pow(2, N, MOD) - 2) % MOD
    part2 = pow(2, K, MOD)
    result = (part1 * part2 + 2) % MOD

    print(result)

if __name__ == "__main__":
    main()