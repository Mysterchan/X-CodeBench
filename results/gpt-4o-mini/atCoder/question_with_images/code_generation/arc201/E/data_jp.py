def calculate_bounding_box_area_sum(N, Y):
    MOD = 998244353
    total_area_sum = 0

    # Precompute the contribution of each point
    for i in range(N):
        x = i + 1
        y = Y[i]
        
        # Count how many subsets can include this point
        left_count = x  # Points to the left (1 to x)
        right_count = N - x  # Points to the right (x+1 to N)
        down_count = y  # Points below (1 to y)
        up_count = N - y  # Points above (y+1 to N)

        # Each point contributes to (left_count * right_count) * (down_count * up_count)
        contribution = (left_count * right_count % MOD) * (down_count * up_count % MOD) % MOD
        area = (contribution * (2 * y - 1) % MOD) * (2 * x - 1) % MOD
        
        total_area_sum = (total_area_sum + area) % MOD

    return total_area_sum

# Input reading
N = int(input())
Y = list(map(int, input().split()))

# Calculate and print the result
result = calculate_bounding_box_area_sum(N, Y)
print(result)