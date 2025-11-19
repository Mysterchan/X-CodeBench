N = int(input())
A = list(map(int, input().split()))

is_strictly_increasing = True
for i in range(1, N):
    if A[i-1] >= A[i]:
        is_strictly_increasing = False
        break

print("Yes" if is_strictly_increasing else "No")