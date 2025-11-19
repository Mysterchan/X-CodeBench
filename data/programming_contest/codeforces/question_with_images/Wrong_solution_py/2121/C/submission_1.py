import sys

t=int(sys.stdin.readline())
for i in range(t):
    r,c=list(map(int,sys.stdin.readline().split()))
    l=[]
    for _ in range(r):
        l.append(list(map(int,sys.stdin.readline().split())))
    item=max(max(i) for i in l)

    lst=[]
    if r==1 or c==1:
        print(int(item)-1)
    else:
        for i in range(r):
            for j in range(c):
                if l[i][j]==item:
                    lst.append((i,j))

        if len(lst)<3:
            print(int(item)-1)
        else:
            r1=lst[0][0]
            c1=lst[1][1]
            r2=lst[1][0]
            c2=lst[0][1]
            if lst[2][0]==r1 or lst[2][1]==c1:
                r=r1
                c=c1
            elif lst[2][0]==r2 or lst[2][1]==c2:
                r=r2
                c=c2
            else:
                print(item)
                continue
            for i in lst:
                if i[0]==r or i[1]==c:
                    pass
                else:
                    print(item)
                    break
            else:
                print(int(item)-1)
