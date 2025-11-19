a1, a2, a3 = map(int, input().split())

nums = [a1, a2, a3]

found = False
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                if nums[i] * nums[j] == nums[k]:
                    found = True
                    break
        if found:
            break
    if found:
        break

if found:
    print("Yes")
else:
    print("No")