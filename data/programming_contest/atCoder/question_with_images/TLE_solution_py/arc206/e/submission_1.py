def gen(N, K):
    if 2 * K > N:
        return []
    cand = [[]]
    for _ in range(K):
        ncand = []
        for p in cand:
            use = [0] * N
            for x, y in p:
                use[x] = 1
                use[y] = 1
            if len(p) == 0:
                lim = -1
            else:
                lim = p[-1][0]
            for l in range(lim + 1, N):
                for r in range(l + 1, N):
                    if use[l] == use[r] == 0:
                        np = p[:]
                        np.append((l, r))
                        ncand.append(np)
        cand = ncand
    return cand

import itertools

def naive(N, U, D, L, R):

    cand = []
    for i in range(1, N - 1):
        cand.append((0, i, U[i]))
        cand.append((N - 1, i, D[i]))
        cand.append((i, 0, L[i]))
        cand.append((i, N - 1, R[i]))

    ans = 1 << 60
    t = 0

    for p in gen(len(cand), 4) + gen(len(cand), 5):
        mat = [[0] * N for i in range(N)]
        cost = 0
        for u, v in p:
            x1, y1, c1 = cand[u]
            x2, y2, c2 = cand[v]
            cost += c1 + c2
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    mat[x][y] = 1
        flag = 1
        for x in range(N):
            for y in range(N):
                flag &= mat[x][y]
        if flag:
            ans = min(ans, cost)
    return ans

inf = 1 << 60

def sub(N, A, B):
    dp = [[inf] * 3 for i in range(3)]
    dp[0][0] = 0

    for i in range(1, N - 1):
        ndp = [[inf] * 3 for i in range(3)]
        for j in range(3):
            for k in range(3):
                if j == 2 and k == 0:
                    pass
                else:
                    ndp[j][k] = dp[j][k]
        for j in range(3):
            for k in range(3):
                for dj in range(2):
                    for dk in range(2):
                        if j + dj >= 3 or k + dk >= 3:
                            continue
                        val = dp[j][k]
                        if dj == 1:
                            val += A[i]
                        if dk == 1:
                            val += B[i]
                        ndp[j + dj][k + dk] = min(ndp[j + dj][k + dk], val)
        dp = ndp

    return dp[2][2]

def calc(N, U, D, L, R):
    sU = sorted([(U[i], i) for i in range(N)])
    sD = sorted([(D[i], i) for i in range(N)])
    sL = sorted([(L[i], i) for i in range(N)])
    sR = sorted([(R[i], i) for i in range(N)])

    ans = 1 << 60

    mU = sU[1][0]
    posU = sU[1][1]
    for i in range(N):
        if U[i] <= mU:
            posU = i

    mD = sD[1][0]
    posD = sD[1][1]
    for i in range(N - 1, -1, -1):
        if D[i] <= mD:
            posD = i

    mL = sU[1][0]
    posL = sL[1][1]
    for i in range(N - 1, -1, -1):
        if U[i] <= mL:
            posL = i

    mR = sR[1][0]
    posR = sR[1][1]
    for i in range(N):
        if R[i] <= mR:
            posR = i

    ans0 = inf
    if posU + 1 < posD and posR + 1 < posL:
        pass
    else:
        ans0 = sU[0][0] + sU[1][0] + sD[0][0] + sD[1][0] + sL[0][0] + sL[1][0] + sR[0][0] + sR[1][0]

    ans1 = sU[0][0] + sU[1][0] + sD[0][0] + sD[1][0] + sL[0][0] + sL[1][0] + sR[0][0] + sR[1][0] + (sU[2][0] + sD[2][0])
    ans2 = sU[0][0] + sU[1][0] + sD[0][0] + sD[1][0] + sL[0][0] + sL[1][0] + sR[0][0] + sR[1][0] + (sR[2][0] + sL[2][0])

    ans3 = sub(N, U, D) + sL[0][0] + sL[1][0] + sR[0][0] + sR[1][0]
    ans4 = sub(N, R, L) + sU[0][0] + sU[1][0] + sD[0][0] + sD[1][0]
    return min(ans0, ans1, ans2, ans3, ans4)

import random

random.seed(0)

while 0:
    N = random.randint(4, 5)
    U = [1 << 60] + [random.randint(1, 100) for i in range(N - 2)] + [1 << 60]
    D = [1 << 60] + [random.randint(1, 100) for i in range(N - 2)] + [1 << 60]
    L = [1 << 60] + [random.randint(1, 100) for i in range(N - 2)] + [1 << 60]
    R = [1 << 60] + [random.randint(1, 100) for i in range(N - 2)] + [1 << 60]

    ans1 = min(calc(N, U, D, L, R), calc(N, U[::-1], D[::-1], L[::-1], R[::-1]))
    ans2 = naive(N, U, D, L, R)
    print(N, ans1, ans2)
    assert ans1 == ans2

for _ in range(int(input())):
    N = int(input())
    U = [1 << 60] + list(map(int, input().split())) + [1 << 60]
    D = [1 << 60] + list(map(int, input().split())) + [1 << 60]
    L = [1 << 60] + list(map(int, input().split())) + [1 << 60]
    R = [1 << 60] + list(map(int, input().split())) + [1 << 60]
    ans1 = calc(N, U, D, L, R)
    ans2 = calc(N, U[::-1], D[::-1], L[::-1], R[::-1])
    print(min(ans1, ans2), naive(N, U, D, L, R))