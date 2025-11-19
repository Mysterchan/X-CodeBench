n=int(input())
nums=sorted(list(map(int, input().split())))
count=0
j=0
for i in range(n):
    while j<n and nums[j]<2*nums[i]:
        j+=1
    count+=n-j
print(count)