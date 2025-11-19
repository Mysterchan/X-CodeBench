import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    S = [input().strip() for _ in range(N)]
    S.sort(key=len)
    print(''.join(S))

if __name__ == "__main__":
    main()