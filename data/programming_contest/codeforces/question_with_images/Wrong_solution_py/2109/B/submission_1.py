import sys
import math

t=int(sys.stdin.readline())
for i in range(t):
    n,m,a,b=list(map(int,sys.stdin.readline().split()))
    print(min(int(math.log2(min(abs(n-a+1),(a))))+int(math.log2(m)),int(math.log2(min(abs(m-b+1),(b))))+int(math.log2(n)))+1)
