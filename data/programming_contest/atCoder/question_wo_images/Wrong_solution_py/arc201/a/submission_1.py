import sys

def normalize(triple):
    x0, x1, x2 = triple

    x0 = min(x0, x1)

    x2 = min(x2, x1)
    return [x0, x1, x2]

def solve_one(n, triples):
    a = [normalize(row) for row in triples]

    a.sort(key=lambda x: -x[0])

    total0 = sum(x[0] for x in a)

    def ok(mid: int) -> bool:

        cl = 0
        cr = 0
        for x0, x1, x2 in a:
            if cl + x0 <= mid:

                cl += x0

                cr += min(x1 - x0, x2)
            else:

                need = mid - cl
                if need < 0:
                    need = 0
                take0 = min(x0, need)
                cl += take0

                rem1 = x1 - take0
                if rem1 < 0:
                    rem1 = 0
                cr += min(rem1, x2)

            if cl >= mid and cr >= mid:
                return True
        return (cl >= mid) and (cr >= mid)

    l, r = 0, total0 + sum(min(x[1]-x[0], x[2]) for x in a) + 1
    while l + 1 < r:
        m = (l + r) // 2
        if ok(m):
            l = m
        else:
            r = m

    return l

def main():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        triples = [[int(next(it)), int(next(it)), int(next(it))] for _ in range(n)]
        out.append(str(solve_one(n, triples)))
    print("\n".join(out))

if __name__ == "__main__":
    main()