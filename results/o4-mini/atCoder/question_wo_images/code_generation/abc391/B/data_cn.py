def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = [input().rstrip() for _ in range(N)]
    T = [input().rstrip() for _ in range(M)]

    for a in range(N - M + 1):
        for b in range(N - M + 1):
            match = True
            for i in range(M):
                if S[a + i][b:b + M] != T[i]:
                    match = False
                    break
            if match:
                print(a + 1, b + 1)
                return

if __name__ == "__main__":
    main()