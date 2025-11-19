import sys

def main():
    data = sys.stdin.read().split()
    N, M = map(int, data[:2])
    A = set(map(int, data[2:]))

    missing = [str(i) for i in range(1, N+1) if i not in A]
    C = len(missing)

    # Output the count
    print(C)
    # Output the missing numbers in ascending order (empty line if none)
    if C > 0:
        print(" ".join(missing))

if __name__ == "__main__":
    main()