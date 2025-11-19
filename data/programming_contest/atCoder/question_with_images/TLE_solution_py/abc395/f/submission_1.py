import sys
input = sys.stdin.buffer.readline

def main():
    N, X = map(int, input().split())
    teeth = [tuple(map(int, input().split())) for _ in range(N)]

    def check(H: int) -> bool:
        L, R = 0, H
        for U, D in teeth:
            L = max(L + D, H + X, X + D) - X - D
            R = min(R + X, U)
            if L > R:
                return False
        return True

    R = min(U + D for U, D in teeth) + 1
    L = min(X, R - 1)

    while L + 1 < R:
        M = (L + R) // 2
        if check(M):
            L = M
        else:
            R = M

    ans = sum(U + D for U, D in teeth) - L * N
    print(ans)

if __name__ == "__main__":
    main()