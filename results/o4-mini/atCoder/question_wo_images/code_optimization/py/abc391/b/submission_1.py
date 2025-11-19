import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [input().rstrip() for _ in range(N)]
    T = [input().rstrip() for _ in range(M)]
    
    limit = N - M + 1
    for a in range(limit):
        for b in range(limit):
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