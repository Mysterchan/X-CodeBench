A = list(map(int, input().split()))
target = [1, 2, 3, 4, 5]

count = 0
for i in range(4):
    # Create a copy and swap adjacent elements
    B = A[:]
    B[i], B[i+1] = B[i+1], B[i]
    
    # Check if it matches the target
    if B == target:
        count += 1

if count == 1:
    print("Yes")
else:
    print("No")