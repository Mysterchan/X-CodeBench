for _ in range(int(input())):
    n,m,k=map(int,input().split());c={}
    for _ in range(k):
        x,y=map(int,input().split());c[y]=c.get(y,0)^1
    f=False
    if n==1:f=c.get(2,0)&1
    else:
        for a,b in c.items():
            if a>=2 and b&1:f=True;break
    print("Mimo" if f else "Yuyu")
