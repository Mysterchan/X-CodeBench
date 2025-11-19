for _ in range(int(input())):
    n = int(input())
    l = [0] * n
    r = [0] * n
    for i in range(n):
        l[i], r[i] = map(int, input().split())
    ans = [-1] * n
    for p in reversed(range(n)):
        for i in reversed(range(n)):
            if ans[i] != -1:
                continue
            ok = True
            for j in range(n):
                ok &= ans[j] != -1 or not l[j] < l[i] < r[i] < r[j]
            if not ok:
                continue
            ans[i] = p + 1
            break
    print(*ans)