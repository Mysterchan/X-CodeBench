import sys
input = sys.stdin.readline

def reflect(vx, vy, side):
    # side: 0 - vertical (x=0)
    #       1 - horizontal (y=0)
    #       2 - hypotenuse (x+y=n)
    if side == 0:
        return -vx, vy
    elif side == 1:
        return vx, -vy
    else:
        # reflect (vx, vy) about line x+y=0 (normal vector (1,1))
        # reflection formula: v' = v - 2*(v·n)/|n|^2 * n
        # n = (1,1), |n|^2=2
        dot = vx + vy
        vx_new = vx - 2*dot/2
        vy_new = vy - 2*dot/2
        return int(vx_new), int(vy_new)

def solve():
    t = int(input())
    for _ in range(t):
        n,x,y,vx,vy = map(int, input().split())
        # The triangle vertices:
        # A(0,0), B(0,n), C(n,0)
        # Initial point strictly inside: x>0,y>0,x+y<n
        # Velocity vector vx, vy >0

        # We simulate the motion with reflections until:
        # - plane hits a vertex exactly -> output number of boundary hits before that
        # - or detect cycle -> output -1

        # Because n can be large, and velocities large, we must do math, not step simulation.

        # The triangle sides:
        # side0: x=0 (vertical)
        # side1: y=0 (horizontal)
        # side2: x+y=n (hypotenuse)

        # At each step:
        # Find time to each side (if moving towards it)
        # time = (distance to side) / (velocity component towards side)
        # Choose minimal positive time

        # If at that time plane hits vertex -> done
        # Else reflect velocity and continue

        # To avoid infinite loops, store states (x,y,vx,vy) visited

        visited = set()
        count = 0

        # Use float for time, but all inputs are integers, so time will be rational.
        # To avoid floating errors, use fractions or careful float.

        from math import isclose

        # We'll use fractions for exactness
        from fractions import Fraction

        # Convert all to Fraction
        x = Fraction(x)
        y = Fraction(y)
        vx = Fraction(vx)
        vy = Fraction(vy)
        n = Fraction(n)

        # State key: (x,y,vx,vy) as tuple of numerator and denominator to avoid float issues
        def state_key(x,y,vx,vy):
            return (x.numerator,x.denominator,y.numerator,y.denominator,vx.numerator,vx.denominator,vy.numerator,vy.denominator)

        while True:
            key = state_key(x,y,vx,vy)
            if key in visited:
                # cycle detected
                print(-1)
                break
            visited.add(key)

            # Compute times to sides:
            times = []

            # side0: x=0
            if vx < 0:
                t0 = (x) / (-vx)
                times.append( (t0, 0) )
            # side1: y=0
            if vy < 0:
                t1 = (y) / (-vy)
                times.append( (t1, 1) )
            # side2: x+y=n
            # distance to side2 = n - (x+y)
            # velocity towards side2 = vx + vy
            if vx + vy > 0:
                t2 = (n - (x + y)) / (vx + vy)
                times.append( (t2, 2) )

            if not times:
                # no side reachable, plane moves inside forever
                print(-1)
                break

            # minimal positive time
            t_min, side = min(times, key=lambda z: z[0])

            # Move to collision point
            x_new = x + vx * t_min
            y_new = y + vy * t_min

            # Check if collision point is vertex
            # vertices: (0,0), (0,n), (n,0)
            # Use exact comparison with Fraction
            if (x_new == 0 and y_new == 0) or (x_new == 0 and y_new == n) or (x_new == n and y_new == 0):
                # plane escapes
                print(count)
                break

            # else collision with side (not vertex)
            # increment count
            count += 1

            # reflect velocity
            if side == 0:
                vx = -vx
                # vy unchanged
            elif side == 1:
                vy = -vy
                # vx unchanged
            else:
                # reflect about line x+y=n
                # normal vector n = (1,1)
                dot = vx + vy
                vx = vx - dot
                vy = vy - dot

            # update position
            x = x_new
            y = y_new

solve()