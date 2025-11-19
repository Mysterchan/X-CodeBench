def min_cost_to_good_sequence(N, P, C):
    # Create a list of tuples (size, color) and sort it by size
    slimes = sorted(zip(P, C))
    
    # Extract the sorted colors
    sorted_colors = [color for _, color in slimes]
    
    # Create a mapping of color to their positions in the sorted order
    from collections import defaultdict
    color_positions = defaultdict(list)
    for index, color in enumerate(sorted_colors):
        color_positions[color].append(index)
    
    # Create a list to track the current position of each color
    current_positions = [0] * N
    for index, color in enumerate(C):
        current_positions[index] = color_positions[color].pop(0)
    
    # Now we need to find the minimum cost to make the current_positions sorted
    # We will use a Fenwick Tree (Binary Indexed Tree) to count inversions
    class FenwickTree:
        def __init__(self, size):
            self.size = size
            self.tree = [0] * (size + 1)
        
        def add(self, index, value):
            while index <= self.size:
                self.tree[index] += value
                index += index & -index
        
        def sum(self, index):
            total = 0
            while index > 0:
                total += self.tree[index]
                index -= index & -index
            return total
        
        def range_sum(self, left, right):
            return self.sum(right) - self.sum(left - 1)
    
    # Count inversions in current_positions
    fenwick = FenwickTree(N)
    inversions = 0
    for pos in current_positions:
        inversions += fenwick.range_sum(pos + 1, N)
        fenwick.add(pos + 1, 1)
    
    # To minimize the cost, we need to change colors of the slimes
    # We will calculate the cost of changing colors
    cost = 0
    for index in range(N):
        if current_positions[index] != index:
            cost += C[index]
    
    return cost + inversions

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