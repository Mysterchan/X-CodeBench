h,w=map(int,input().split())
M=998244353
a=0
from math import gcd
f=1
if w%2:
  for i in range(h+1):
    if gcd(w,abs(i-(h-i)))==1:
      a+=f
      a%=M
    f*=(h-i)*pow(i+1,M-2,M)
    f%=M
else:
  for i in range(h*2+1):
    if gcd(w//2,abs(i-(h*2-i))//2)==1:
      a+=f
      a%=M
    f*=(h*2-i)*pow(i+1,M-2,M)
    f%=M
print(a*(gcd(h,2)==1))