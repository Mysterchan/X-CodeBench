def count_balls_in_pockets(test_cases):
    results = []
    
    for n, s, shots in test_cases:
        count = 0
        
        for d_x, d_y, x_i, y_i in shots:
            # Calculate how far the ball will go in each direction
            if d_x == 1:
                time_x = (s - x_i) * 1  # time to hit the right wall
            else:
                time_x = x_i * 1  # time to hit the left wall

            if d_y == 1:
                time_y = (s - y_i) * 1  # time to hit the top wall
            else:
                time_y = y_i * 1  # time to hit the bottom wall

            # Determine which wall is hit first
            if time_x < time_y:
                # The ball will hit a vertical wall first
                if d_x == 1:
                    # Moving right hits the right wall
                    final_x, final_y = s, y_i + (s - x_i) * d_y
                else:
                    # Moving left hits the left wall
                    final_x, final_y = 0, y_i + (x_i * d_y)
            else:
                # The ball will hit a horizontal wall first
                if d_y == 1:
                    # Moving up hits the top wall
                    final_x, final_y = x_i + (s - y_i) * d_x, s
                else:
                    # Moving down hits the bottom wall
                    final_x, final_y = x_i + (y_i * d_x), 0
            
            # Check if the ball lands in one of the pockets
            if (final_x, final_y) in {(0, 0), (0, s), (s, 0), (s, s)}:
                count += 1
        
        results.append(count)
    
    return results


# Read data and execute the function
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n, s = map(int, data[index].split())
    shots = []
    for i in range(n):
        shots.append(tuple(map(int, data[index + i + 1].split())))
    test_cases.append((n, s, shots))
    index += n + 1

results = count_balls_in_pockets(test_cases)

for result in results:
    print(result)