n,m=map(int,input().split())
s=[]
t=[]
flag=False
for i in range(n):
    s.append(input().strip())
for i in range(m):
    t.append(input().strip())
for i in range(n-m+1):
    j=0
    while s[i][j:].find(t[0])!=-1:
        j=s[i][j:].find(t[0])
        for k in range(1,m):
            if s[i+k][j:j+m] not in t[k]:
                j+=1
                break
        else:
            print(i+1,j+1)
            flag=True
            break
    if flag:
        break