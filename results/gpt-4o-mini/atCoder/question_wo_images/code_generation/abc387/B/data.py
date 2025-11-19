X = int(input())
total_sum = 0
not_X_sum = 0

# Calculate the sum of the 9x9 multiplication table
for i in range(1, 10):
    for j in range(1, 10):
        value = i * j
        total_sum += value
        if value != X:
            not_X_sum += value

print(not_X_sum)