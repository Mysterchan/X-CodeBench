n = int(input())
p = list(map(int, input().split()))

# Convert to 0-indexed for easier handling
p = [x - 1 for x in p]

total_cost = 0

# Use bubble sort approach to count the minimum cost
# For each position, bubble the correct element to it
for target in range(n):
    # Find where element 'target' currently is
    current_pos = p.index(target)
    
    # Bubble it left to position 'target'
    while current_pos > target:
        # Swap positions current_pos-1 and current_pos
        # Cost is current_pos (in 1-indexed terms)
        p[current_pos - 1], p[current_pos] = p[current_pos], p[current_pos - 1]
        total_cost += current_pos  # current_pos is already 1-indexed cost
        current_pos -= 1

print(total_cost)