import sys
import threading

def solve():
    import sys
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    R = [0]*q
    X = [0]*q
    for i in range(q):
        R[i] = int(next(it))
        X[i] = int(next(it))

    # Coordinate‐compress A_i and X_i together
    vals = set(A)
    vals.update(X)
    vs = sorted(vals)
    m = len(vs)
    comp = {v:i+1 for i,v in enumerate(vs)}

    compA = [comp[a] for a in A]
    compX = [comp[x] for x in X]

    # Prepare queries sorted by R
    # Each query: (R_i, compX_i, original_index)
    queries = [(R[i], compX[i], i) for i in range(q)]
    queries.sort(key=lambda x: x[0])

    # Fenwick tree (1..m) for prefix‐max
    BIT = [0] * (m+1)

    def bit_query(pos):
        """Return max over BIT[1..pos]."""
        res = 0
        b = BIT
        while pos > 0:
            if b[pos] > res:
                res = b[pos]
            pos -= pos & -pos
        return res

    def bit_update(pos, val):
        """Set BIT[pos] = max(BIT[pos], val), propagate upward."""
        b = BIT
        M = m
        while pos <= M:
            if b[pos] < val:
                b[pos] = val
            pos += pos & -pos

    ans = [0] * q
    cur_q = 0

    # Process the array, build dp on the fly and answer queries at each prefix R
    for i in range(1, n+1):
        ai = compA[i-1]
        # Compute dp[i]: 1 + max dp so far for values < A[i]
        best = bit_query(ai-1)
        dpi = best + 1
        # Insert dp[i] into Fenwick
        bit_update(ai, dpi)

        # Answer all queries with R == i
        while cur_q < q and queries[cur_q][0] == i:
            _, cx, qi = queries[cur_q]
            # Maximum dp[j] for j <= i and A[j] <= X[qi]
            ans[qi] = bit_query(cx)
            cur_q += 1

    # Output answers in original order
    out = '\n'.join(str(x) for x in ans)
    sys.stdout.write(out)

if __name__ == "__main__":
    solve()