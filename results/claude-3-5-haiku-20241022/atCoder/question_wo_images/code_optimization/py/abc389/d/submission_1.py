import math

R = int(input())

ans = 0
R_squared = R * R

for i in range(1, R):
    i_plus = i + 0.5
    i_minus = i - 0.5
    
    # Binary search for maximum j
    ok = 0
    ng = R
    
    while ng - ok > 1:
        mid = (ok + ng) // 2
        j_plus = mid + 0.5
        
        # Check the farthest corner: (i+0.5, j+0.5)
        dist_squared = i_plus * i_plus + j_plus * j_plus
        
        if dist_squared <= R_squared:
            ok = mid
        else:
            ng = mid
    
    ans += ok

ans *= 4
ans += 4 * (R - 1) + 1
print(ans)