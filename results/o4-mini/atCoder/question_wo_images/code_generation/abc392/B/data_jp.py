def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    missing = [str(i) for i in range(1, N+1) if i not in A]

    print(len(missing))
    print(" ".join(missing))


if __name__ == "__main__":
    main()