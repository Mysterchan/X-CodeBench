import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    strs = [input().strip() for _ in range(N)]
    strs.sort(key=len)
    print("".join(strs))

if __name__ == "__main__":
    main()