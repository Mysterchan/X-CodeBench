for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(n):
        a, b, c, d = map(int, input().split())
        if b>d: ans+= a + (b-d)
        elif a>c: ans+=c-a
    print(ans)
