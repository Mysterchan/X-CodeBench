import sys,bisect

input=lambda: sys.stdin.readline().strip()
lst=[]
n=int(input())
for i in range(n):
    l,r=map(int,input().split())
    lst.append([min(l,r),max(l,r)])
lst.sort(key=lambda x:x[1])
right_end_sort_ans=[0]*(2*n+1)
left_end_sort_ans=[0]*(2*n+1)
info=[]
ans=0
for i in lst:
    now=i[0]
    if not info or now<info[0]:
        bisect.insort(info,now)
        ans+=1
    else:
        pos=bisect.bisect_left(info,now)

        info[pos-1]=now
    right_end_sort_ans[i[1]]=ans

ans=0
lst.sort(key=lambda x:x[0],reverse=True)
info=[]
for i in lst:
    now=i[0]
    if not info or now>info[-1]:
        bisect.insort(info,now)
        ans+=1
    else:
        pos=bisect.bisect_left(info,now)
        info[pos]=now
    left_end_sort_ans[i[0]]=ans

cur=0
for i in range(1,len(right_end_sort_ans)):
    cur=max(cur,right_end_sort_ans[i])
    right_end_sort_ans[i]=cur
cur=0
for i in range(len(left_end_sort_ans)-1,0,-1):
    cur=max(cur,left_end_sort_ans[i])
    left_end_sort_ans[i]=cur

ans=0
for border in range(1,2*n+1):
    if border==2*n:
        ans=max(ans,right_end_sort_ans[2*n])
    else:
        ans=max(ans,right_end_sort_ans[border]+left_end_sort_ans[border+1])

print(ans)