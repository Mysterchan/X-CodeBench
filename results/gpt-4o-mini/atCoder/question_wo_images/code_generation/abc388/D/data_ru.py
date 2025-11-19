N = int(input())
A = list(map(int, input().split()))

B = [0] * N
current_stones = 0

for i in range(N):
    if i > 0:
        current_stones += A[i - 1] - (1 if A[i - 1] > 0 else 0)
    B[i] = A[i] + current_stones

print(' '.join(map(str, B)))