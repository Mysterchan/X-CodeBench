N, K = map(int, input().split())
A = list(map(int, input().split()))
nums = [0 for _ in range(10 ** 6 + 1)]
n_test = 0
A_set = set()
for x in A:
    nums[x] += 1
    if x > n_test:
        n_test = x
    A_set.add(x)
diviser = [[] for _ in range(n_test + 1)]
encount = [0 for _ in range(n_test + 1)]
encount[1] = N
for i in range(1, n_test + 1):
    counter = i
    while counter <= n_test:
        if counter in A_set:
            diviser[counter].append(i)
            encount[i] += nums[counter]
        counter += i
for i in range(N):
    if A[i] == 1:
        print(1)
        continue
    maxs = 1
    for x in diviser[A[i]]:
        if encount[x] >= K and x > maxs:
            maxs = x
    print(maxs)