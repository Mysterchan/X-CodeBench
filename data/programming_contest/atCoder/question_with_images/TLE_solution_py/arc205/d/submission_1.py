import sys;sys.setrecursionlimit(9**9);x=[*open(0)][:0:-1]
def f(i,s=0):
 (m,q),_=max(((l:=f(j),s:=s+l[1])for j in g[i]),default=((0,0),0))
 p=s&1;return(m-p>s-q+p)*(m-s+q-p)+p+1,s+1
while x:
 n=int(x.pop());g=[[]for i in" "*-~n];c=2
 for i in x.pop().split():g[int(i)]+=c,;c+=1
 print(n-f(1)[0]>>1)