X = int(input())

count = 0
i = 1
while i <= 9 and i * i <= X:
    if X % i == 0:
        j = X // i
        if j <= 9:
            if i == j:
                count += 1
            else:
                count += 2
    i += 1

print(2025 - count * X)