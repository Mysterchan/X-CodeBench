import sys
import math

t=int(sys.stdin.readline())
for i in range(t):
    n,m,a,b=list(map(int,sys.stdin.readline().split()))
    print(min(math.ceil(math.log2(min(abs(n-a+1),(a))))+math.ceil(math.log2(m)),math.ceil(math.log2(min(abs(m-b+1),(b))))+math.ceil(math.log2(n)))+1)
