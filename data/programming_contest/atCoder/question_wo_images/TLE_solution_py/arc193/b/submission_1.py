N = int(input())
S = [int(a) for a in input()]
P = 998244353
X = [0] * 16
X[9] = 1
for i in range(N):
    nX = [0] * 16
    for k in range(16):
        nb = [0] * 4
        for used in range(2):
            for used_first in range(2):
                if not k >> (used * 2 + used_first) & 1:
                    continue
                nused_first = used_first
                for nused in range(2):
                    if i == N - 1 and nused != used_first:
                        continue
                    for a in range(S[i] + 1):
                        nval = (1 - used) + nused + a
                        nb[nval] |= 1 << (nused * 2 + nused_first)
        for nval in range(4):
            nk = nb[nval]
            nX[nk] = (nX[nk] + X[k]) % P
    X = nX
print((sum([x for k, x in enumerate(X) if k])) % P)