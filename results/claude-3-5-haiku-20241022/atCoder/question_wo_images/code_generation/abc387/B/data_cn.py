X = int(input())

total = 0
for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        if product != X:
            total += product

print(total)