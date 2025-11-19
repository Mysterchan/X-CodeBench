l = list(map(int,input().split()))
ans = 0
for i in range(5):
    for j in range(i+1,5):
        if l[i]>l[j]:
            ans += 1
if ans == 1:
    print("Yes")
else:
    print("No")