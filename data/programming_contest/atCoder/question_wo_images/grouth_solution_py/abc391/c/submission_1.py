n, q = map(int, input().split())

place = [i for i in range(n)]
cnt = [1] * n
ans = 0
for _ in range(q):
    t, *ph = map(int, input().split())
    if t == 1:
        p = ph[0]-1
        h = ph[1]-1

        old_h = place[p]
        place[p] = h

        if cnt[old_h] == 2:
            ans -= 1
        cnt[old_h] -= 1

        if cnt[h] == 1:
            ans += 1
        cnt[h] += 1
    else:
        print(ans)