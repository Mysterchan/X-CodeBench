def get_dis(s: str):
    d = []
    for i in range(len(s)):
        if s[i] == '1':
            d.append(i)
    for i in range(len(d) - 1):
        d[i] = d[i + 1] - d[i];
    d.pop()
    return d

def get_pos(s: str):
    for i in range(len(s)):
        if s[i] == '1':
            return i

def solve(a: list, b: list, delta: int):

    c = []
    cnt0 = len(a) - len(b)
    res = 0
    cur = 0
    tag = 0
    for i in range(len(a)):
        if cur >= len(b) or a[i] < b[cur]:
            if cnt0 > 0:
                cnt0 -= 1
                c.append(0)
            else:
                return 1919810
        else:
            c.append(b[cur])
            cur += 1
        if (a[i] - c[i] - tag)%2 == 1:
            c[i] += 1
            if i + 1 < len(a):
                tag = 1
            else:
                tag = 0
            delta += 1
            res += 1

    for i in range(len(a)):
        res += (a[i] - c[i]) // 2
        delta += (a[i] - c[i]) // 2
    return res + abs(delta);

T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    s1 = input()
    s2 = input()
    a = get_dis(s1)
    b = get_dis(s2)

    if len(a) < len(b):
        print(-1)
        continue
    pos1 = get_pos(s1)
    pos2 = get_pos(s2)

    if len(a) == 0:
        print(abs(pos2 - pos1))
        continue
    ans = solve(a, b, pos1 - pos2)
    a[0] -= 1
    ans = min(ans, 1 + solve(a, b, pos1 - pos2))
    if ans == 1919810:
        print(-1)
    else:
        print(ans)