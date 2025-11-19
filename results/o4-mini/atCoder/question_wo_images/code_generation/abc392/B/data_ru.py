import sys

def main():
    data = sys.stdin.read().strip().split()
    N, M = map(int, data[:2])
    A = set(map(int, data[2:2+M]))
    missing = [str(i) for i in range(1, N+1) if i not in A]
    print(len(missing))
    if missing:
        print(" ".join(missing))

if __name__ == "__main__":
    main()