def min_steps_to_reach(t, test_cases):
    results = []
    for x, y in test_cases:
        # We want to check the minimum steps required to reach (x, y)
        step = 1
        total_x, total_y = 0, 0
        
        while total_x < x or total_y < y:
            if step % 2 == 1:  # odd step, move in x direction
                total_x += step
            else:  # even step, move in y direction
                total_y += step

            if total_x >= x and total_y >= y:
                # Check conditions for reaching (x, y)
                if total_x == x and total_y == y:
                    results.append(step)
                    break
                elif total_x > x or total_y > y:
                    results.append(-1)
                    break
            
            step += 1
            
        if total_x < x or total_y < y:
            results.append(-1)

    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(t)]

# Get results
results = min_steps_to_reach(t, test_cases)

# Output results
for result in results:
    print(result)