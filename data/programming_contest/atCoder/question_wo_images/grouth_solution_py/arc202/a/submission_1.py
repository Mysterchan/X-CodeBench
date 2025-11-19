import sys

int1 = lambda x: int(x)-1
pDB = lambda *x: print(*x, end="\n", file=sys.stderr)
p2D = lambda x: print(*x, sep="\n", end="\n\n", file=sys.stderr)
def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def SI(): return sys.stdin.readline().rstrip()

dij = [(0, 1), (-1, 0), (0, -1), (1, 0)]

inf = -1-(-1 << 62)

def RLE(s):
    kk=[]
    vv=[]
    for c in s:
        if kk and kk[-1]==c:
            vv[-1]+=1
        else:
            kk.append(c)
            vv.append(1)
    return kk,vv

def op(d,c):
    if d==0:return c,0
    if c==1:return 1,d
    cnt,cost=op(d-1,(c+(c&1))//2)
    return cnt,(c&1)+cost

def solve():
    n=II()
    aa=LI()
    aa,cc=RLE(aa)
    n=len(aa)
    ll=list(range(-1,n-1))
    rr=list(range(1,n+1))
    ia=sorted(enumerate(aa),key=lambda x:x[1])
    ans=0
    for i,a in ia:
        if aa[i]!=a:continue
        mn=inf
        l,r=ll[i],rr[i]
        if l>=0 and aa[l]<mn:mn=aa[l]
        if r<n and aa[r]<mn:mn=aa[r]
        if mn==inf:break
        cnt,cost=op(mn-a,cc[i])
        ans+=cost
        aa[i]=-1
        if l>=0:rr[l]=r
        if r<n:ll[r]=l
        if l>=0 and aa[l]==mn:
            cc[l]+=cnt
        else:
            cc[r]+=cnt
        if l>=0 and r<n and aa[l]==aa[r]:
            aa[r]=-1
            cc[l]+=cc[r]
            r2=rr[r]
            rr[l]=r2
            if r2<n:ll[r2]=l
    i=0
    while aa[i]==-1:i+=1
    c=cc[i]
    while c>1:
        ans+=c&1
        c+=c&1
        c>>=1
    print(ans)

for _ in range(II()):solve()