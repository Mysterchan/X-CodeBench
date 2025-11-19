R = int(input())
R_squared = R * R

count = 0

# For each non-negative i, find the maximum j
max_i = int(R - 0.5)  # Maximum possible i value

for i in range(max_i + 1):
    # Find maximum j such that (i+0.5)^2 + (j+0.5)^2 <= R^2
    # (j+0.5)^2 <= R^2 - (i+0.5)^2
    
    i_contrib = (i + 0.5) ** 2
    if i_contrib > R_squared:
        break
    
    remaining = R_squared - i_contrib
    
    # Find largest j where (j+0.5)^2 <= remaining
    max_j = int((remaining ** 0.5) - 0.5)
    
    if max_j < 0:
        continue
    
    # Count squares for this i value
    for j in range(max_j + 1):
        j_contrib = (j + 0.5) ** 2
        if i_contrib + j_contrib <= R_squared:
            # Count based on quadrant symmetry
            if i == 0 and j == 0:
                count += 1
            elif i == 0:
                count += 2  # j and -j
            elif j == 0:
                count += 2  # i and -i
            else:
                count += 4  # all four quadrants

print(count)