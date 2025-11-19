import sys
import threading
import numpy as np

MOD = 998244353

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    Ps = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    for i in range(M):
        Ps[i] = [x - 1 for x in Ps[i]]

    pos = []
    for P in Ps:
        posP = [0]*N
        for i, x in enumerate(P):
            posP[x] = i
        pos.append(posP)

    allowed = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ok = True
            for k in range(M):
                pi = pos[k][i]
                pj = pos[k][j]

                if (pi < pj and pj - pi == 1) or (pi == N-1 and pj == 0):
                    continue
                elif (pj < pi and pi - pj == 1) or (pj == N-1 and pi == 0):
                    continue
                else:
                    ok = False
                    break
            if ok:
                allowed[i][j] = True

    L = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            if i != j and allowed[i][j]:
                L[i][i] += 1
                L[i][j] -= 1

    mat = L[1:, 1:]
    ans = int(round(np.linalg.det(mat))) % MOD
    print(ans)

threading.Thread(target=main).start()