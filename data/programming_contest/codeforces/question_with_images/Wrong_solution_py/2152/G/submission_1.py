import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

class SegmentTree:
    def __init__(self, n):
        self.N = 1
        while self.N < n: self.N <<= 1
        self.data = [0]*(2*self.N)
        self.lazy = [0]*(2*self.N)
    def build(self, arr):
        for i,v in enumerate(arr):
            self.data[self.N+i] = v
        for i in range(self.N-1,0,-1):
            self.data[i] = self.data[i*2]+self.data[i*2+1]
    def push(self, node,l,r):
        if self.lazy[node]:
            self.data[node] = (r-l+1)-self.data[node]
            if node < self.N:
                self.lazy[node*2]^=1
                self.lazy[node*2+1]^=1
            self.lazy[node]=0
    def update(self,L,R,node=1,l=0,r=None):
        if r is None: r=self.N-1
        self.push(node,l,r)
        if r<L or R<l: return
        if L<=l and r<=R:
            self.lazy[node]^=1
            self.push(node,l,r)
            return
        m=(l+r)//2
        self.update(L,R,node*2,l,m)
        self.update(L,R,node*2+1,m+1,r)
        self.data[node]=self.data[node*2]+self.data[node*2+1]
    def query(self):
        self.push(1,0,self.N-1)
        return self.data[1]

def main():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        edges=[[] for _ in range(n)]
        for _ in range(n-1):
            u,v=map(int,input().split())
            edges[u-1].append(v-1)
            edges[v-1].append(u-1)
        q=int(input())
        queries=[int(input())-1 for _ in range(q)]

        in_order=[0]*n
        out_order=[0]*n
        order=0
        parent=[-1]*n
        stack=[(0,-1)]
        children=[[] for _ in range(n)]
        while stack:
            v,p=stack.pop()
            in_order[v]=order
            order+=1
            parent[v]=p
            for u in reversed(edges[v]):
                if u!=p:
                    children[v].append(u)
                    stack.append((u,v))
        out_order=[0]*n
        def dfs_out(v):
            o=in_order[v]
            for u in children[v]:
                o=dfs_out(u)
            out_order[v]=o
            return o
        dfs_out(0)

        st=SegmentTree(n)
        st.build(a)
        print(st.query())
        for v in queries:
            st.update(in_order[v],out_order[v])
            print(st.query())

main()
