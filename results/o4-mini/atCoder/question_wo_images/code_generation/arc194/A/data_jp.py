N = int(input())
A = list(map(int, input().split()))

S = []
total_sum = 0

for a in A:
    if a > 0:
        S.append(a)
        total_sum += a
    elif S:
        # Only pop if S is not empty
        S.pop()

print(total_sum)