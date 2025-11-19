from sortedcontainers import SortedList

n,q = map(int,input().split())

sl = SortedList()
sl.add([1,n])
for _ in range(q):
    a,b = map(int,input().split())
    idx_a = sl.bisect_right([a,n+1])
    idx_b = sl.bisect_right([b,n+1])
    if idx_a != idx_b:
        print("No")
        continue
    print("Yes")
    idx = idx_a-1
    l,r = sl[idx]
    sl.discard(sl[idx])
    sl.add([l,a])
    sl.add([a,b])
    sl.add([b,r])