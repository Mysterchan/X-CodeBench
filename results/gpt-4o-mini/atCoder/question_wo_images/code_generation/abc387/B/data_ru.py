X = int(input())
total_sum = 0

for i in range(1, 10):
    for j in range(1, 10):
        value = i * j
        if value != X:
            total_sum += value

print(total_sum)