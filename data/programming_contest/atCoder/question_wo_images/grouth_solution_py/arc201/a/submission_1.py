T = int(input())
for _ in range(T):
    n = int(input())
    q = []
    hset = []
    mset = []
    eset = []
    for i in range(n):
        h,m,e = map(int,input().split())
        hset.append(min(h,m))
        eset.append(min(m,e))
        mset.append(min(h + e,m))
    print(min(sum(hset),sum(eset),sum(mset)//2))