X = int(input())

total_sum = 2025
count = 0

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == X:
            count += 1

print(total_sum - X * count)