t = int(input())
for i in range(t):
    n, r_k, c_k, r_d, c_d = map(int, input().split())

    if r_d > r_k:
        top = (r_d - r_k) // 2
        bottom = r_d
    else:
        top = n - r_d
        bottom = (r_k - r_d) // 2

    if c_d > c_k:
        left = (c_d - c_k) // 2
        right = c_d
    else:
        left = n - c_d
        right = (c_k - c_d) // 2

    if abs(r_d - r_k) == 1 and abs(c_d - c_k) == 0:
        print(max(top, bottom))
    elif abs(c_d - c_k) == 1 and abs(r_d - r_k) == 0:
        print(max(left, right))
    else:
        print(max(top, bottom, left, right))
