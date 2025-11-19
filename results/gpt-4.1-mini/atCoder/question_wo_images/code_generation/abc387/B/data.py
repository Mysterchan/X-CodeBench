X = int(input())

total_sum = 0
for i in range(1, 10):
    for j in range(1, 10):
        val = i * j
        if val != X:
            total_sum += val

print(total_sum)