def sum_of_bounding_boxes(N, Y):
    MOD = 998244353
    
    # Precompute the number of subsets for each possible range
    total_subsets = (1 << N) - 1  # 2^N - 1
    total_subsets_minus_one = (1 << (N - 1)) - 1  # 2^(N-1) - 1
    
    # To store the total area
    total_area = 0
    
    # Calculate the contribution of each point
    for i in range(N):
        # The x-coordinate is i + 1 (1-based index)
        x = i + 1
        y = Y[i]
        
        # Count how many subsets can be formed with this point as the leftmost or rightmost
        left_count = i + 1  # Points to the left including this point
        right_count = N - i  # Points to the right including this point
        
        # Each point contributes to the area of bounding boxes
        # The area contributed by this point being the leftmost or rightmost
        contribution = (y * (right_count * left_count) % MOD) * (total_subsets_minus_one) % MOD
        
        # Add the contribution to the total area
        total_area = (total_area + contribution) % MOD
    
    # Each area is counted twice (once for each order of leftmost and rightmost)
    total_area = (total_area * 2) % MOD
    
    return total_area

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
Y = list(map(int, data[1:]))

# Output the result
print(sum_of_bounding_boxes(N, Y))