n = int(input())
p = list(map(int, input().split()))

total_cost = 0

for i in range(n - 1):
    needs_swap = False
    for j in range(i + 1):
        for k in range(i + 1, n):
            if p[j] > p[k]:
                needs_swap = True
                break
        if needs_swap:
            break
    
    if needs_swap:
        total_cost += i + 1

print(total_cost)