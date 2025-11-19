X = int(input())
total_sum = 0

for i in range(1, 10):  # From 1 to 9
    for j in range(1, 10):  # From 1 to 9
        product = i * j
        if product != X:
            total_sum += product

print(total_sum)