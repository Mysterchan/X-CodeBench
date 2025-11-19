def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    strings = [input().rstrip('\n') for _ in range(n)]
    strings.sort(key=len)
    print(''.join(strings))


if __name__ == "__main__":
    main()