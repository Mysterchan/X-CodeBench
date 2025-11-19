X = int(input())
total = 0
for i in range(1, 10):
    for j in range(1, 10):
        val = i * j
        if val != X:
            total += val
print(total)