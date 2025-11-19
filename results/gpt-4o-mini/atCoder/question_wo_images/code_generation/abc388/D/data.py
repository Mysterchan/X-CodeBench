def final_stones(n, A):
    # Create an array B to store the final number of stones for each alien
    B = [0] * n
    
    # Initialize the sum of stones to distribute each year
    stones_to_distribute = 0
    
    for year in range(n):
        # The current alien that is becoming an adult
        adult_index = year
        # Count the stones to distribute from those who are already adults
        stones_to_distribute += A[adult_index]  # Add the current adult's stones
        
        if year > 0:
            # Subtract one stone for every adult who has at least one stone
            # All previous adults are year-1 or earlier
            for i in range(adult_index):
                if B[i] > 0:
                    B[i] -= 1
        
        # The current alien receives stones from all adults
        B[adult_index] += stones_to_distribute
    
    # Print the final result
    print(" ".join(map(str, B)))

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))

final_stones(N, A)