n, m = map(int, input().split())
acc = [0]*2*n
for _ in range(m):
    a, b = map(int, input().split())
    acc[a-1] += 1
    acc[b-1] -= 1
for i in range(2*n-1):
    acc[i+1] += acc[i]
groups = [None]*2*n
g = 0
flg = False
for i in range(2*n):
    if not flg and acc[i] > 0:
        flg = True
    elif flg and acc[i]==0:
        flg = False
        g += 1
    groups[i] = g
q = int(input())
for _ in range(q):
    c, d = map(int, input().split())
    c, d = c-1, d-1
    if groups[c] == groups[d]:
        ans = abs(acc[c] - acc[d])
    else:
        ans = abs(acc[c] + acc[d])
    print(ans)