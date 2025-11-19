R = int(input())
sx = 0.5
sy = 0.5
x = R
ans = 0
import math
for y in range(1,R+1):
    while x > 0:
        if math.hypot(x - sx,y - sy) <= R:
            ans += x
            break
        else:
            x -= 1
print(ans*4 - 3 - (R-1)*4)