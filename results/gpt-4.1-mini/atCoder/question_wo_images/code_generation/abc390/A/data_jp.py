A = list(map(int, input().split()))
target = [1, 2, 3, 4, 5]

for i in range(4):
    A[i], A[i+1] = A[i+1], A[i]
    if A == target:
        print("Yes")
        break
    A[i], A[i+1] = A[i+1], A[i]
else:
    print("No")