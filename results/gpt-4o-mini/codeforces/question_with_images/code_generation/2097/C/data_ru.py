def will_plane_escape(num_tests, test_cases):
    results = []
    
    for n, x, y, v_x, v_y in test_cases:
        count = 0
        
        # The equations of lines from the triangle vertices
        # y = -x + n, x = 0, y = 0
        while True:
            if (x == 0 and y == 0) or (x == 0 and y == n) or (x == n and y == 0):
                results.append(count)
                break
                
            # Time to hit the x = 0 boundary
            if v_x < 0:  # it's moving towards left
                time_to_left = x / -v_x
            else:
                time_to_left = float('inf')
            
            # Time to hit the y = 0 boundary
            if v_y < 0:  # it's moving towards bottom
                time_to_bottom = y / -v_y
            else:
                time_to_bottom = float('inf')
            
            # Time to hit the hypotenuse y = -x + n
            if v_x - v_y != 0:  # to avoid division by zero
                time_to_hypotenuse = (n - x) / (v_x - v_y) if v_x > v_y else (n - y) / (v_y - v_x)
            else:
                time_to_hypotenuse = float('inf')
            
            # Find the minimum time to hit a boundary
            min_time = min(time_to_left, time_to_bottom, time_to_hypotenuse)
            
            # If the minimum time is infinite, it means it will never exit
            if min_time == float('inf'):
                results.append(-1)
                break
            
            # Calculate new position after min_time
            new_x = x + min_time * v_x
            new_y = y + min_time * v_y
            
            # Determine which boundary was hit
            if min_time == time_to_left:
                x = 0
                y = new_y
                count += 1
                # Reflect velocity
                v_x = -v_x
            elif min_time == time_to_bottom:
                x = new_x
                y = 0
                count += 1
                # Reflect velocity
                v_y = -v_y
            else:
                # for the hypotenuse
                if v_x > v_y:
                    x_h = n - y
                    y = n - x
                    x = x_h
                else:
                    y_h = n - x
                    x = n - y
                    y = y_h
                count += 1
                # Reflect velocity
                v_x, v_y = -v_y, -v_x
                
            # Now check if it hits a vertex
            if (x == 0 and y == 0) or (x == 0 and y == n) or (x == n and y == 0):
                results.append(count)
                break
            
            # Update original coordinates
            x, y = new_x, new_y

    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(t)]

# Get results
results = will_plane_escape(t, test_cases)

# Print results
for result in results:
    print(result)