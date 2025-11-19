from collections import deque, Counter
import random
import bisect

def ril():
    return map(int, input().split())

T = int(input())

for t in range(T):
    n, M = ril()
    a = list(ril())
    b = list(ril())

    b_eq = len(set(b)) == 1
    a_eq = len(set(a)) == 1

    a.sort()
    b.sort()

    cb = Counter(b)
    for x in a:
        y = M-x if x else 0
        if cb[y] > 0:
            cb[y] -= 1
        else:
            break
    else:
        print(0)
        continue

    l = 1
    r = M-1

    iR = [0] * n
    iL = [0] * n
    while l < r:
        m = (l+r)//2

        L = R = 0

        R = bisect.bisect_right(b, m)
        nR = R + n
        def f(R):
            if R < n:
                return b[R] - M
            else:
                return b[R - n]

        for i in range(n-1, -1, -1):
            while R < nR and a[i] + f(R) <= m:
                R += 1
            iR[i] = R

        for i in range(n-1, -1, -1):
            while L < n and b[L] + a[i] < M:
                L += 1

            iL[i] = L
            if iR[i] < L: iR[i] += n
            if iR[i] == iL[i] == n:
                if (a[i] + b[0]) % M <= m:
                    iR[i] += n

        intervals = list(zip(iL, iR))

        cL = cR = -2*n
        ml, mr = min(intervals)

        prev = (-n, -n)
        def process(i):
            global cL, cR, prev
            L, R = iL[i], iR[i]
            if not (L >= prev[0] or L == R or prev[0] == prev[1]):
                print(i, L, R, prev)
                assert False
            if not (L == R or L != prev[0] or R >= prev[1] or prev[0] == prev[1]):
                print(i, L, R, prev)
                assert False

            prev = (L, R)
            L -= n-1-i; R -= n-1-i

            if cL == cR == -2*n:
                cL = L; cR = R
            else:
                cL = max(L, cL)
                cR = min(R, cR)

        extra = deque()
        dropped = -1
        for i in range(n-1, -1, -1):

            if i > 0:
                assert iL[i-1] >= iL[i]
                if iL[i-1] == iL[i]:
                    assert iR[i-1] >= iR[i]
            process(i)
            continue

            if i < n-1 and iR[i] < iR[i+1]:
                dropped = i+1
            if dropped >= 0 and iL[i] == iL[dropped]:
                process(i)
            elif dropped >= 0 and iL[i] != iL[dropped]:
                while extra:
                    process(extra.popleft())
                dropped = -1
            else:
                extra.append(i)
            continue
            if iL[i] == iL[start] and i > start:
                extra.append(i)
            elif extra and iL[i] != iL[start]:
                while extra:
                    process(extra.popleft())
                process(i)
            elif i == 0 and extra:
                process(i)
                while extra:
                    process(extra.popleft())
            else:
                process(i)
            if cL >= cR:
                while extra:
                    process(extra.popleft())
                break

        while extra:
            process(extra.popleft())

        if cL < cR:
            r = m
        else:
            l = m+1

    print(l)