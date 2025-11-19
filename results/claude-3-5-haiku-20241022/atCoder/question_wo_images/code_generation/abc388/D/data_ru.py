n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    adults_with_stones = sum(1 for j in range(i) if a[j] > 0)
    a[i] += adults_with_stones
    for j in range(i):
        if a[j] > 0:
            a[j] -= 1

print(' '.join(map(str, a)))