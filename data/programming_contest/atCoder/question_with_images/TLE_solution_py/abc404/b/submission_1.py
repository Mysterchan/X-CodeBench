n=int(input())
sl=[]
tl=[]
for i in range(n):
    sn=input()
    sl.append(sn)
for i in range(n):
    tn=input()
    tl.append(tn)

s=[]
t=[]
for i in range(n):
    for j in range(n):

        if sl[i][j]=="#":
            s.append([i,j])
        if tl[i][j]=="#":
            t.append([i,j])
def change(N,l):
    for i in range(len(l)):

        l[i][0],l[i][1]=l[i][1],N-1-l[i][0]
count=0
ans=999999999
for i in range(4):
    now=count
    right=0
    for j in range(len(s)):
        if s[j] not in t:
            now+=1
        else:
            right+=1
    now+=len(t)-right
    if ans>now:
        ans=now

    change(n,s)

    count+=1
print(ans)