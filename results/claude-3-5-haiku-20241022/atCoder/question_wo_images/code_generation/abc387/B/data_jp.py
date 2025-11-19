X = int(input())

total = 0
for i in range(1, 10):
    for j in range(1, 10):
        value = i * j
        if value != X:
            total += value

print(total)