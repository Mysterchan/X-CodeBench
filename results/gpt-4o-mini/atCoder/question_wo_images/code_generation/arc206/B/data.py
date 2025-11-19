def min_cost_to_good_sequence(N, P, C):
    # Create a list of tuples (size, color) and sort by size
    slimes = sorted(zip(P, C))
    
    # Extract the colors in the order of sorted sizes
    sorted_colors = [color for _, color in slimes]
    
    # We need to find the minimum cost to make the sorted_colors a good sequence
    # A good sequence means that we can sort the colors by swapping adjacent different colors
    # We will use a greedy approach to change colors to the most frequent color in the sorted list
    
    from collections import Counter
    
    # Count the frequency of each color in the sorted_colors
    color_count = Counter(sorted_colors)
    
    # Find the most frequent color
    most_frequent_color, max_count = color_count.most_common(1)[0]
    
    # Calculate the total cost to change all other colors to the most frequent color
    total_cost = 0
    for color in sorted_colors:
        if color != most_frequent_color:
            total_cost += color  # Cost is the color of the slime before changing
    
    return total_cost

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
P = list(map(int, data[1:N+1]))
C = list(map(int, data[N+1:2*N+1]))

# Get the result
result = min_cost_to_good_sequence(N, P, C)

# Print the result
print(result)