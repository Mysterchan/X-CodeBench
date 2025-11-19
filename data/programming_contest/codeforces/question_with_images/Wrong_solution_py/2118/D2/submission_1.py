import sys
import bisect
from collections import defaultdict


def solve() -> None:
    it = iter(sys.stdin.read().split())
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        k = int(next(it))

        p = [int(next(it)) for _ in range(n)]
        d = [int(next(it)) for _ in range(n)]

        v = [(p[i] - d[i]) % k for i in range(n)]
        u = [(v[i] + 2 * p[i]) % k for i in range(n)]

        v_to_pos = defaultdict(list)
        pos_to_u = {}
        for i in range(n):
            v_to_pos[v[i]].append(p[i])
            pos_to_u[p[i]] = u[i]

        u_to_pos = defaultdict(list)
        for i in range(n):
            u_to_pos[u[i]].append(p[i])
        for lst in u_to_pos.values():
            lst.sort()

        trap_intervals = defaultdict(list)

        for res, lst in v_to_pos.items():
            m = len(lst)
            for i in range(m - 1):
                L = lst[i]
                R = lst[i + 1]

                if ((R - L) * 2) % k != 0:
                    continue

                uL = pos_to_u[L]

                inner = u_to_pos.get(uL, [])
                idx = bisect.bisect_right(inner, L)
                if idx < len(inner) and inner[idx] < R:
                    continue

                trap_intervals[res].append((L, R))

        lefts = {}
        rights = {}
        for res, intervals in trap_intervals.items():
            lefts[res] = [l for l, _ in intervals]
            rights[res] = [r for _, r in intervals]
        q = int(next(it))
        for _ in range(q):
            a = int(next(it))
            r = a % k

            Llist = lefts.get(r, [])
            if not Llist:
                out.append("YES")
                continue

            idx = bisect.bisect_right(Llist, a) - 1
            if idx < 0:
                out.append("YES")
                continue

            l, rr = Llist[idx], rights[r][idx]
            if l <= a <= rr:
                out.append("NO")
            else:
                out.append("YES")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
