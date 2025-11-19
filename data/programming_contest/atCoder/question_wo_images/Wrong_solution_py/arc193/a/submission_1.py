inf = 10**18
N = int(input())
W = [int(x) for x in input().split()]

kukan = []
for i in range(N):
    l, r = map(int, input().split())
    kukan.append((i, l, r, W[i]))
L = [l for _, l, _, _ in kukan]
R = [r for _, _, r, _ in kukan]

RR = sorted(kukan, key= lambda x: x[2])
pre_min = [x[3] for x in RR]
for i in range(1, N):
    pre_min[i] = min(pre_min[i], pre_min[i-1])
i2RR = {i:k for k, (i, _, _, _) in enumerate(RR)}

LL = sorted(kukan, key= lambda x: x[1])
suf_min = [x[3] for x in LL]
for i in range(N - 2, 0, -1):
    suf_min[i] = min(suf_min[i], suf_min[i+1])
i2LL = {i:k for k, (i, _, _, _) in enumerate(LL)}

def hidari(x, i):
    left = -1
    right = N
    while right - left > 1:
        mid = (right + left) // 2
        if RR[mid][2] < x:
            left = mid
        else:
            right = mid
    return pre_min[left] if 0 <= left < i else inf

def migi(x, i):
    left = -1
    right = N
    while right - left > 1:
        mid = (right + left) // 2
        if x < LL[mid][1]:
            right = mid
        else:
            left = mid
    return suf_min[right] if i < right < N else inf

Q = int(input())
ANS = []
for _ in range(Q):
    s, t = map(int, input().split())
    s, t = s-1, t-1
    if L[s] > L[t]:
        s, t = t, s
    ans = W[s] + W[t]
    if R[s] < L[t]:
        ANS.append(ans)
    else:
        w1 = hidari(L[s], i2RR[s])
        w2 = migi(R[t], i2LL[t])
        w = min(w1, w2)
        if w == inf:
            ANS.append(-1)
        else:
            ANS.append(ans + w)
print(*ANS, sep="\n")