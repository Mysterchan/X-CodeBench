N = int(input())
A = list(map(int, input().split()))

if N == 2:
    print("Yes")
    exit()

# 比率を分数で比較するために分子と分母を使う
# 公比は A[1]/A[0]
from math import gcd

num = A[1]
den = A[0]
g = gcd(num, den)
num //= g
den //= g

for i in range(2, N):
    # 比較対象の比率 A[i]/A[i-1]
    n = A[i]
    d = A[i-1]
    g = gcd(n, d)
    n //= g
    d //= g
    if n * den != num * d:
        print("No")
        break
else:
    print("Yes")