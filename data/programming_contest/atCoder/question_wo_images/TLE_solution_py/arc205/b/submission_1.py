n,m=map(int,input().split())
def h(x,y):return min(x<<20|y,y<<20|x)
g={h(*map(int,input().split()))for i in range(m)}
while len(g)>1:
    a,b=divmod(g.pop(),1048576)
    c,d=divmod(g.pop(),1048576)
    if b==d:g^={h(a,c)}
    elif a==c:g^={h(b,d)}
    elif a==d:g^={h(b,c)}
    elif b==c:g^={h(a,d)}
    else:g^={h(a,c)}
print((n*n-n>>1)-len(g))