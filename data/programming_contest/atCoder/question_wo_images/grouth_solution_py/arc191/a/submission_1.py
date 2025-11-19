N,M=list(map(int,input().split()))
S=list(input())
T=list(input())
nums=[0]*10
for t in T:
    nums[int(t)]+=1
num=9
while nums[num]==0:
    num-=1
for i in range(N):
    if num==0:
        break
    if int(S[i])<num:
        S[i]=str(num)
        nums[num]-=1
        while num>=1 and nums[num]==0:
            num-=1
if nums[int(T[-1])]:
    ok=False
    for i in range(N):
        if S[i]==T[-1]:
            ok=True
    if not ok:
        S[-1]=T[-1]
print("".join(S))