import sys
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    A = set()
    for _ in range(M):
        try:
            A.add(int(next(it)))
        except StopIteration:
            break
    missing = [str(i) for i in range(1, N+1) if i not in A]
    sys.stdout.write(str(len(missing)) + "\n")
    if missing:
        sys.stdout.write(" ".join(missing))

if __name__ == "__main__":
    main()