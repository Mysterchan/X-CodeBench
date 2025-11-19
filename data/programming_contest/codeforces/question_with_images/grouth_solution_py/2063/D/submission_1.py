for _ in range(int(input())):
    x, y = map(int, input().split())
    p, q = sorted(map(int, input().split())), sorted(map(int, input().split()))
    u, v = [0], [0]
    for i in range(x // 2): u.append(u[-1] + p[-1 - i] - p[i])
    for i in range(y // 2): v.append(v[-1] + q[-1 - i] - q[i])
    z, k = [], 1
    while True:
        a, b = max(0, 2 * k - y), min(k, x - k)
        if a > b: break
        while a + 3 < b:
            c, d = (a * 2 + b) // 3, (a + b * 2) // 3
            b = d if u[c] + v[k - c] > u[d] + v[k - d] else b
            a = c if u[c] + v[k - c] <= u[d] + v[k - d] else a
        z.append(max(u[e] + v[k - e] for e in range(a, b + 1)))
        k += 1
    print(len(z))
    print(*z)
