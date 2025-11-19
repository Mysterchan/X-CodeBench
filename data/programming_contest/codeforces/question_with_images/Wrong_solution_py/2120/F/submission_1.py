import sys

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        for _ in range(k):
            m = int(next(it))
            for _ in range(m):
                u = next(it)
                v = next(it)
        out_lines.append("Yes")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
