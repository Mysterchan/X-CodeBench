R = int(input())

ans = 0

# Count the number of squares whose centers are completely inside the circle
for i in range(R):
    # Calculate the maximum j value such that the center of the square (i+0.5, j+0.5) is within the circle
    max_j = int((R**2 - (i + 0.5) ** 2) ** 0.5 - 0.5)
    if max_j < 0:
        break
    ans += max_j + 1

# There are 4 quadrants, so multiply by 4
ans *= 4

# Add the squares along the axes and the center square
ans += 4 * (R - 1) + 1

print(ans)