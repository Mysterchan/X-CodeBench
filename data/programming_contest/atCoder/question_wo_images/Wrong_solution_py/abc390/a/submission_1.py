A = list(map(int, input().split()))
c = 0
for i in range(5):
    if A[i] != i + 1:
        c += 1
if c == 2:
    print('Yes')
else:
    print('No')