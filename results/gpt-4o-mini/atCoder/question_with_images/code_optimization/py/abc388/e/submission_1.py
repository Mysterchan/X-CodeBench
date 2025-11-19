N = int(input())
A = list(map(int, input().split()))

count = 0
j = 0

for i in range(N):
    while j < N and A[j] < 2 * A[i]:
        j += 1
    count += (N - j)

print(count // 2)