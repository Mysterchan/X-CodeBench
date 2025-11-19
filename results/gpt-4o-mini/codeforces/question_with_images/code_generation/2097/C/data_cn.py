def count_hits(t, cases):
    results = []
    
    for n, x, y, v_x, v_y in cases:
        if v_x == 0 and v_y == 0:
            results.append(-1)
            continue
            
        total_hits = 0
        
        # Check if the direction will make the plane escape immediately
        if (x + v_x == 0 and y + v_y == 0) or (x + v_x == n and y + v_y == 0) or \
           (x + v_x == 0 and y + v_y == n) or (x + v_x == n and y + v_y == n):
            results.append(0)
            continue
        
        while True:
            # Compute time to each wall
            if v_x > 0:
                tx = (n - x) / v_x
            elif v_x < 0:
                tx = -x / v_x
            else:
                tx = float('inf')  # The plane will never hit the vertical walls if v_x == 0
            
            if v_y > 0:
                ty = (n - y) / v_y
            elif v_y < 0:
                ty = -y / v_y
            else:
                ty = float('inf')  # The plane will never hit the horizontal walls if v_y == 0
            
            t_min = min(tx, ty)
            if t_min == float('inf'):
                break
            
            # Move the airplane to the next hit point
            x += v_x * t_min
            y += v_y * t_min
            
            total_hits += 1
            
            if x == 0 or x == n or y == 0 or y == n:
                break
            
            # Reflect the direction upon hitting the wall
            if tx < ty:  # Hitting vertical wall
                x = n if v_x > 0 else 0
                v_x = -v_x
            else:  # Hitting horizontal wall
                y = n if v_y > 0 else 0
                v_y = -v_y
            
        if x == 0 and y == 0 or x == n and y == 0 or x == 0 and y == n or x == n and y == n:
            results.append(total_hits)
        else:
            results.append(-1)
    
    return results

# Input reading
t = int(input())
cases = [tuple(map(int, input().split())) for _ in range(t)]
results = count_hits(t, cases)

# Output results
for result in results:
    print(result)