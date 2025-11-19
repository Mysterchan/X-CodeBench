from sortedcontainers import SortedList
from operator import itemgetter

class Mo:
    def __init__(self, ls):
        from math import sqrt, ceil
        self.ls = ls.copy()
        self.n = len(ls)
        self.b = ceil(sqrt(self.n))

    def _init_states(self):

        self.having = SortedList()

        self.l = 0
        self.r = 0

        self.bucket = [list() for _ in range((self.b + 1))]

    def _add(self, i):

        self.having.add(A[i])

    def _delete(self, i):

        self.having.remove(A[i])

    def _one_process(self, l, r):

        for i in range(self.r, r):
            self._add(i)
        for i in range(self.r - 1, r - 1, -1):
            self._delete(i)
        for i in range(self.l, l):
            self._delete(i)
        for i in range(self.l - 1, l - 1, -1):
            self._add(i)

        self.l = l
        self.r = r

    def process(self, queries):
        self._init_states()

        for i, (l, r) in enumerate(queries):
            self.bucket[l // self.b].append((l, r, i))

        for i in range(len(self.bucket)):
            self.bucket[i].sort(key=itemgetter(1))

        ret = [-1] * len(queries)
        for b in self.bucket:
            for l, r, i in b:
                self._one_process(l, r)

                ok,ng = 0,(r-l)//2+1
                while(ng - ok > 1):
                    mid = (ok+ng)//2

                    ue = list(self.having[:mid])
                    shita = list(self.having[-mid:])
                    flag = True
                    for j in range(mid):
                        if(ue[j]*2 > shita[j]):
                            flag = False
                            break
                    if(flag):
                        ok = mid
                    else:
                        ng = mid
                ret[i] = ok

        return ret

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
query = []
for _ in range(Q):
    l,r = list(map(int,input().split()))
    l -= 1;r -= 1
    query.append((l,r+1))

mo = Mo(A).process(query)
for i in mo:
    print(i)