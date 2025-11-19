n = int(input())
p = [0]+list(map(int, input().split()))
q = [0]+list(map(int, input().split()))

ans = []

for i in range(1, n+1):
    x = q.index(i)
    l = p[x]
    ans.append(q.index(l))

print(*ans)