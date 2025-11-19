def main():
    import sys
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    A = set(map(int, data[2:]))

    missing = []
    for i in range(1, N + 1):
        if i not in A:
            missing.append(str(i))

    print(len(missing))
    if missing:
        print(" ".join(missing))


if __name__ == "__main__":
    main()