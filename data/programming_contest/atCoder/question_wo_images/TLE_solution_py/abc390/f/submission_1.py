def fLR(l, r):
    global A
    global AN

    for i in range(l, r + 1):
        AN[A[i]] = 1

    f = False
    bfr = 0
    cnt = 0
    for i in range(1, N + 2):
        if AN[i] == 1:
            if f == False:
                f = True
                bfr = i
            else:
                if i == bfr + 1:
                    bfr = i
                else:
                    cnt += 1
                    f = False
            AN[i] = 0
        else:
            if f == True:
                cnt += 1
            f = False

    return cnt

N = int(input())

A = list(map(int, input().split()))

AN = [0] * (N + 2)

sum = 0
for i in range(0, N):
    for j in range(i, N):
        sum += fLR(i, j)

print(sum)