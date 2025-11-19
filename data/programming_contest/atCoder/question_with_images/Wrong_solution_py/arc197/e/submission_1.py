import sys

def solve():
    N, H, W = map(int, sys.stdin.readline().split())

    MOD = 998244353

    def count_ways(Dim, TileN):
        if Dim < 2 * TileN:
            return 0

        term1 = Dim - 2 * TileN + 1
        term2 = Dim - 2 * TileN + 2

        result = (term1 * term2 // 2) % MOD
        return result

    ways_h = count_ways(H, N)
    ways_w = count_ways(W, N)

    ans = (ways_h * ways_w) % MOD

    print(ans)

def main():
    try:
        T = int(sys.stdin.readline())
        for _ in range(T):
            solve()
    except (IOError, ValueError):
        pass

if __name__ == "__main__":
    main()