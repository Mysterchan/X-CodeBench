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
            encount[i] += nums[counter]
        counter += i
ans = [1 for _ in range(n_test + 1)]
for i in range(1, n_test + 1):
    if encount[i] < K:
        continue
    ans[i] = i
    for j in range(2 * i, n_test + 1, i):
        ans[j] = max(ans[j], i)
for i in range(N):
    print(ans[A[i]])