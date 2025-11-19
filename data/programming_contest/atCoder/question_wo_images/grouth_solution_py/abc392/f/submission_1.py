n = int(input())
P = list(map(lambda x: int(x)-1, input().split()))

from sortedcontainers import SortedList

SL = SortedList([i for i in range(n)])

A = [0]*n

for i in range(n)[::-1]:
    p = P[i]
    s = SL.pop(p)
    A[s] = i+1

print(*A)