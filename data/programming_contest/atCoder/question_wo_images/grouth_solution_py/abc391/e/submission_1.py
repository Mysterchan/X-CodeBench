import sys
from array import array
def solve() -> None:
    data = sys.stdin.read().split()
    N = int(data[0])
    A = ''.join(data[1:])
    L = 3 ** N
    total_nodes = (3 ** (N + 1) - 1) // 2
    leaf_start = (L - 1) // 2
    dp0 = array('I', [0]) * total_nodes
    dp1 = array('I', [0]) * total_nodes
    for i in range(leaf_start, total_nodes):
        idx = i - leaf_start
        ch = A[idx]
        dp0[i] = 0 if ch == '0' else 1
        dp1[i] = 0 if ch == '1' else 1
    INF = 10 ** 9
    for i in range(leaf_start - 1, -1, -1):
        c1 = 3 * i + 1
        c2 = 3 * i + 2
        c3 = 3 * i + 3
        best0 = dp0[c1] + dp0[c2] + dp0[c3]
        cost = dp1[c1] + dp0[c2] + dp0[c3]
        if cost < best0:
            best0 = cost
        cost = dp0[c1] + dp1[c2] + dp0[c3]
        if cost < best0:
            best0 = cost
        cost = dp0[c1] + dp0[c2] + dp1[c3]
        if cost < best0:
            best0 = cost
        dp0[i] = best0
        best1 = dp1[c1] + dp1[c2] + dp0[c3]
        cost = dp1[c1] + dp0[c2] + dp1[c3]
        if cost < best1:
            best1 = cost
        cost = dp0[c1] + dp1[c2] + dp1[c3]
        if cost < best1:
            best1 = cost
        cost = dp1[c1] + dp1[c2] + dp1[c3]
        if cost < best1:
            best1 = cost
        dp1[i] = best1
    cur = list(map(int, A))
    for _ in range(N):
        nxt = []
        for i in range(0, len(cur), 3):
            s = cur[i] + cur[i + 1] + cur[i + 2]
            nxt.append(1 if s > 1 else 0)
        cur = nxt
    orig_root = cur[0]
    if orig_root == 0:
        ans = dp1[0]
    else:
        ans = dp0[0]
    print(ans)
if __name__ == '__main__':
    solve()