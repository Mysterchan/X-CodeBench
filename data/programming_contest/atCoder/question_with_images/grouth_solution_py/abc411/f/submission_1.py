def main():
    class UnionFind:

        _N: int
        _parent: list[int]

        def __init__(self, N: int):
            self._N = N
            self._parent = [-1] * N
        def find(self, Vi: int):
            Pi = Vi
            while self._parent[Pi] >= 0: Pi = self._parent[Pi]
            while Pi != Vi: self._parent[Vi], Vi = Pi, self._parent[Vi]
            return Pi
        def unite(self, Ui: int, Vi: int):
            if ( Ui := self.find(Ui) ) == ( Vi := self.find(Vi) ): return False
            if self._parent[Ui] > self._parent[Vi]: Ui, Vi = Vi, Ui
            self._parent[Ui] += self._parent[Vi]; self._parent[Vi] = Ui
            return True
        def same(self, Ui: int, Vi: int): return self.find(Ui) == self.find(Vi)
        def size(self, Vi: int): return - self._parent[ self.find(Vi) ]

    import sys
    input = lambda: next(iter(sys.stdin))

    N, M = [int(v) for v in input().split()]
    edges = [0] * M
    G = [set() for _ in range(N)]
    for m in range(M):
        Ui, Vi = [int(v) for v in input().split()]
        Ui, Vi = Ui - 1, Vi - 1
        G[Ui].add(Vi)
        G[Vi].add(Ui)
        edges[m] = Ui << 20 | Vi
    Q = int(input())

    UF = UnionFind(N)
    rabel = list(range(N))
    cnt = M
    ans = [''] * Q

    for q, Xi in enumerate(input().split()):
        Xi = int(Xi) - 1
        Ui, Vi = edges[Xi] >> 20, edges[Xi] & 0xFFFFF
        Ui, Vi = UF.find(Ui), UF.find(Vi)
        if Ui == Vi:
            ans[q] = str(cnt)
            continue

        UF.unite(Ui, Vi)
        Pi = UF.find(Ui)
        Ci = Vi if Pi == Ui else Ui
        R_Pi, R_Ci = rabel[Pi], rabel[Ci]
        if len( G[R_Pi] ) < len( G[R_Ci] ):
            rabel[Pi], rabel[Ci] = rabel[Ci], rabel[Pi]
            R_Pi, R_Ci = R_Ci, R_Pi
        for nxt in G[R_Ci]:
            if nxt == R_Pi:

                cnt -= 1
                G[R_Pi].discard(R_Ci)
            elif nxt not in G[R_Pi]:

                G[nxt].discard(R_Ci)
                G[nxt].add(R_Pi)
                G[R_Pi].add(nxt)
            else:

                G[nxt].discard(R_Ci)
                cnt -= 1
        G[R_Ci].clear()
        ans[q] = str(cnt)

    sys.stdout.write('\n'.join(ans))

main()