def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(n, x, y, vx, vy):
    g = gcd(abs(vx), abs(vy))
    vx //= g
    vy //= g

    visited = set()
    reflections = 0

    for _ in range(4 * n + 100):
        if (x == 0 and y == 0) or (x == 0 and y == n) or (x == n and y == 0):
            return reflections

        state = (x, y, vx, vy)
        if state in visited:
            return -1
        visited.add(state)

        t_min = None
        boundary_type = None

        if vx < 0:
            t = -x / vx
            next_y = y + t * vy
            if 0 <= next_y <= n:
                if t_min is None or t < t_min:
                    t_min = t
                    boundary_type = 'left'

        if vy < 0:
            t = -y / vy
            next_x = x + t * vx
            if 0 <= next_x <= n:
                if t_min is None or t < t_min:
                    t_min = t
                    boundary_type = 'bottom'

        if vx + vy > 0:
            t = (n - x - y) / (vx + vy)
            next_x = x + t * vx
            next_y = y + t * vy
            if next_x >= 0 and next_y >= 0:
                if t_min is None or t < t_min:
                    t_min = t
                    boundary_type = 'hypotenuse'

        if boundary_type is None:
            return -1

        x += t_min * vx
        y += t_min * vy

        x = round(x)
        y = round(y)

        if boundary_type == 'left':
            x = 0
            vx = -vx
        elif boundary_type == 'bottom':
            y = 0
            vy = -vy
        else:
            if x + y > n:
                if x > n:
                    x = n
                    y = 0
                elif y > n:
                    y = n
                    x = 0
            elif x + y < n:
                diff = n - x - y
                if abs(diff) < 1e-9:
                    if x > y:
                        x += diff
                    else:
                        y += diff

            vx, vy = -vy, -vx

        reflections += 1

        if reflections > 10**6:
            return -1

    return -1

t = int(input())
for _ in range(t):
    n, x, y, vx, vy = map(int, input().split())
    print(solve(n, x, y, vx, vy))
