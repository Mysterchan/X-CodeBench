def count_squares(R):
    count = 0
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            if (x + 0.5)**2 + (y + 0.5)**2 <= R**2 and (x + 0.5)**2 + (y - 0.5)**2 <= R**2 and (x - 0.5)**2 + (y + 0.5)**2 <= R**2 and (x - 0.5)**2 + (y - 0.5)**2 <= R**2:
                count += 1
    return count

R = int(input())
print(count_squares(R))