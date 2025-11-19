def calculate_hits(n, x, y, v_x, v_y):
    # Check if the airplane can escape directly
    def can_escape(v):
        gx = (n - x) / v[0]  # time to reach vertical edge (y = 0)
        gy = (n - y) / v[1]  # time to reach horizontal edge (x = 0)

        # Adjust for the sides of the triangle
        time_to_hit = max(gx, gy)
        if time_to_hit <= 0:
            return False
        
        x_final = x + v[0] * time_to_hit
        y_final = y + v[1] * time_to_hit
        
        if x_final < 0 or y_final < 0 or x_final + y_final > n:
            return False
        return True

    hits = 0
    initial_velocity_x = v_x
    initial_velocity_y = v_y

    while True:
        if can_escape((v_x, v_y)):
            return hits
        # Calculate the time to hit each border
        time_to_hit_left = float('inf') if v_x >= 0 else -x / v_x
        time_to_hit_bottom = float('inf') if v_y >= 0 else -y / v_y
        time_to_hit_right = float('inf') if v_x <= 0 else (n - x) / v_x
        time_to_hit_top = float('inf') if v_y <= 0 else (n - y) / v_y

        # Determine the next hit
        time_to_next_hit = min(time_to_hit_left, time_to_hit_bottom, time_to_hit_right, time_to_hit_top)

        if time_to_next_hit == float('inf'):
            return -1
        
        hits += 1
        x += v_x * time_to_next_hit
        y += v_y * time_to_next_hit
        
        # Reflect the velocity
        if time_to_next_hit == time_to_hit_left:
            v_x = -v_x
        elif time_to_next_hit == time_to_hit_bottom:
            v_y = -v_y
        elif time_to_next_hit == time_to_hit_right:
            v_x = -v_x
        else:  # time_to_next_hit == time_to_hit_top
            v_y = -v_y

        # Check for boundary conditions
        if x == 0 and (y == 0 or y == n):
            return hits
        if y == 0 and (x == 0 or x == n):
            return hits
        if y == n and (x == 0 or x == n):
            return hits

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n, x, y, v_x, v_y = map(int, data[i].split())
        result = calculate_hits(n, x, y, v_x, v_y)
        results.append(result)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()