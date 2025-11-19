N,L = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
if L%3 == 0:
    now = L//3
    lis = [[0,0,0] for _ in range(now)]

    lis[0][0] += 1

    NN = 0
    for i in range(N-1):
        NN += A[i]
        NN = NN % L
        lis[NN % now][NN // now] += 1

    for i in range(now):
        if 0 not in lis[i]:
            ans += lis[i][0] * lis[i][1] *lis[i][2]

else:
    print(0)

print(ans)