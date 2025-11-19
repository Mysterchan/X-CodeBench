N = int(input().strip())
A = list(map(int, input().strip().split()))

is_strictly_increasing = True
for i in range(1, N):
    if A[i-1] >= A[i]:
        is_strictly_increasing = False
        break

if is_strictly_increasing:
    print("Yes")
else:
    print("No")