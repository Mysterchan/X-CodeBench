import random
from operator import xor

class FenwickTreeInjectable:
    def __init__(self, n, identity_factory, func, rev_func=None):
        self.size = n
        self.tree = [identity_factory() for _ in range(n + 1)]
        self.func = func
        self.rev_func = rev_func
        self.idf = identity_factory
        self.depth = n.bit_length()

    def add(self, i, x):
        i += 1
        tree = self.tree
        func = self.func
        while i <= self.size:
            tree[i] = func(tree[i], x)
            i += i & -i

    def sum(self, i):
        i += 1
        s = self.idf()
        tree = self.tree
        func = self.func
        while i > 0:
            s = func(s, tree[i])
            i -= i & -i
        return s

    def sum_range(self, l, r):
        assert self.rev_func is not None
        assert 0 <= l < r
        result = self.sum(r - 1)
        if l > 0:
            result = self.rev_func(result, self.sum(l - 1))
        return result

    def lower_bound(self, x, lt):

        total = self.idf()
        pos = 0
        tree = self.tree
        func = self.func
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k > self.size:
                continue
            new_total = func(total, tree[k])
            if lt(new_total, x):
                total = new_total
                pos += 1 << i
        return pos + 1, total

    def debug_print(self):
        prev = 0
        arr = []
        for i in range(self.size):
            curr = self.sum(i)
            arr.append(curr - prev)
            prev = curr
        print(arr)

def solve(n, m, q, segments, queries):
    fwd_fwt = FenwickTreeInjectable(n + 1, int, xor, xor)
    bwd_fwt = FenwickTreeInjectable(n + 1, int, xor, xor)
    fwd_s = [0] * (n + 1)
    fwd_t = [0] * (n + 1)
    bwd_s = [0] * (n + 1)
    bwd_t = [0] * (n + 1)
    next_conflict = [m] * m
    zobrist_value = [random.randrange(0, 1 << 60) for _ in range(m)]

    def can_add_segment(s, t):
        if s < t:
            if fwd_s[s] > 0 or fwd_t[t] > 0 or bwd_t[s] > 0 or bwd_s[t] > 0:
                return False
            elif s + 1 < t and fwd_fwt.sum_range(s + 1, t) != 0:
                return False
        else:
            if bwd_s[s] > 0 or bwd_t[t] > 0 or fwd_t[s] > 0 or fwd_s[t] > 0:
                return False
            elif t + 1 < s and bwd_fwt.sum_range(t + 1, s) != 0:
                return False
        return True

    l = 0
    r = 0
    sr, tr = 0, 0
    while r < m:
        while r < m:
            s, t = segments[r]
            s -= 1
            t -= 1
            if can_add_segment(s, t):
                if s < t:
                    fwd_s[s] += 1
                    fwd_t[t] += 1
                    fwd_fwt.add(s, zobrist_value[r])
                    fwd_fwt.add(t, zobrist_value[r])
                else:
                    bwd_s[s] += 1
                    bwd_t[t] += 1
                    bwd_fwt.add(s, zobrist_value[r])
                    bwd_fwt.add(t, zobrist_value[r])
                r += 1
            else:
                sr = s
                tr = t
                next_conflict[l] = r
                break
        else:

            break

        while l < r:
            s, t = segments[l]
            s -= 1
            t -= 1
            if s < t:
                fwd_s[s] -= 1
                fwd_t[t] -= 1
                fwd_fwt.add(s, zobrist_value[l])
                fwd_fwt.add(t, zobrist_value[l])
            else:
                bwd_s[s] -= 1
                bwd_t[t] -= 1
                bwd_fwt.add(s, zobrist_value[l])
                bwd_fwt.add(t, zobrist_value[l])
            l += 1
            if can_add_segment(sr, tr):
                if sr < tr:
                    fwd_s[sr] += 1
                    fwd_t[tr] += 1
                    fwd_fwt.add(sr, zobrist_value[r])
                    fwd_fwt.add(tr, zobrist_value[r])
                else:
                    bwd_s[sr] += 1
                    bwd_t[tr] += 1
                    bwd_fwt.add(sr, zobrist_value[r])
                    bwd_fwt.add(tr, zobrist_value[r])
                r += 1
                break
            else:
                next_conflict[l] = r

    ans = []
    for l, r in queries:
        ans.append(next_conflict[l - 1] >= r)

    return ans

def naive_next_conflict(n, m, q, segments, queries):
    def check(l):
        for i in range(l + 1, m):
            si, ti = segments[i]
            for j in range(l, i):
                sj, tj = segments[j]
                if si < ti and sj < tj:
                    if not (si < sj < tj < ti or sj < si < ti < tj or ti <= sj or tj <= si):
                        break
                elif ti < si and tj < sj:
                    if not (ti < tj < sj < si or tj < ti < si < sj or si <= tj or sj <= ti):
                        break
                else:
                    if si == tj or ti == sj:
                        break
            else:
                continue
            return i
        return m

    next_conflict = [m] * m
    for l in range(m):
        next_conflict[l] = check(l)

    return next_conflict

def check():
    n = 10
    m = 6
    segments = [(i, j) for i in range(1, n + 1) for j in range(1, n + 1) if i != j]
    q = 0
    queries = []
    for _ in range(100):
        segments = random.sample(segments, k=m)
        ans1 = solve(n, m, q, segments, queries)
        ans2 = naive_next_conflict(n, m, q, segments, queries)
        if ans1 == ans2:
            continue
        print('----')
        print(f'{n} {m} {q}')
        print('\n'.join(f'{a[0]} {a[1]}' for a in segments))
        print()
        print(f'{ans1=}')
        print(f'{ans2=}')

n, m, q = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]
queries = [tuple(map(int, input().split())) for _ in range(q)]
ans = solve(n, m, q, segments, queries)
print('\n'.join('Yes' if a else 'No' for a in ans))