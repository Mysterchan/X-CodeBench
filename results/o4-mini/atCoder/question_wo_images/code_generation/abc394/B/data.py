def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    strings = [input().rstrip() for _ in range(N)]
    strings.sort(key=len)

    result = "".join(strings)
    print(result)

if __name__ == "__main__":
    main()