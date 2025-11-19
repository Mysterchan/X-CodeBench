R=lambda:map(int,input().split())
t,=R()
while t:t-=1;R();a,b,c,d=R();l=*R(),((a-c)**2+(b-d)**2)**.5;print('YNeos'[max(l)*2>sum(l)::2])
