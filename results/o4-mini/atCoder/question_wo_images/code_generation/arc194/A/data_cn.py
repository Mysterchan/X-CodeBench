N = int(input())
A = list(map(int, input().split()))

S = []
total_sum = 0

for a in A:
    if a > 0:
        S.append(a)
        total_sum += a
    elif S and a < 0:
        if total_sum + a > total_sum:
            S.append(a)
            total_sum += a
        else:
            if S:
                total_sum -= S.pop()

print(total_sum)