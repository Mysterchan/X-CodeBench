from collections import deque

N,M = map(int,input().split())
S,T = [int(s) for s in input()],input()
HT = [deque([]) for _ in range(10)]
for a in range(M):
    HT[int(T[-1-a])].append(a)

msi = 0
mt = 10**9
m = 11
for a in reversed(range(10)):
    if msi <= N-1:
        while HT[a] and msi <= N-1:
            x = HT[a].popleft()
            while msi <= N-1 and S[msi] >= a:
                m = min(m,S[msi])
                msi += 1
            if msi <= N-1:
                S[msi] = a
                m = min(m,S[msi])
                msi += 1
                mt = min(mt,x)
if mt >= 1:
    t = int(T[-1])
    if m > t:
        S[-1] = t

Ans = ""
for s in S:
    Ans += str(s)
print(Ans)