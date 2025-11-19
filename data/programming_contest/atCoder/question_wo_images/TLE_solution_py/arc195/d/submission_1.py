t = int(input())

def make():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    p = 0
    for a in A:
        if p != a:
            ans += 1
        p = a
    now = 0
    while now+3 < n:
        if A[now] == A[now+1]:
            now += 1
            continue
        if A[now] == A[now+2]:
            if A[now+1] == A[now+3]:
                ans -= 1
                now += 3
            elif now + 5 < n and A[now+1] == A[now+4]:
                mow = now + 3
                while True:
                    if mow + 2 < n and A[mow] == A[mow+2]:
                        ans -= 1
                        now = mow+2
                        break
                    elif mow + 4 < n and A[mow] == A[mow+3]:
                        mow += 3
                    else:
                        now += 1
                        break
            else:
                now += 1

    return ans

for _ in range(t):
    print(make())