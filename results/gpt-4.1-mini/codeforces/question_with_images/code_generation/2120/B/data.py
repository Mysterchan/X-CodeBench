def will_pot_ball(s, dx, dy, x, y):
    # The ball moves at 45 degrees with direction (dx, dy)
    # After reflections, the ball's position can be modeled using "mirrored" tables.
    # The ball will be potted if it reaches a corner (0,0), (0,s), (s,0), or (s,s).
    #
    # The ball's position at time t (without reflections) would be:
    #   (x + dx*t, y + dy*t)
    #
    # Due to reflections, the ball's position modulo 2*s behaves like a "bouncing" coordinate:
    # For coordinate c (x or y), the effective position after reflections is:
    #   pos = c + d*t (mod 2*s)
    #   if pos > s: pos = 2*s - pos
    #
    # The ball is potted if at some time t, pos_x and pos_y are both 0 or s.
    #
    # We want to find t > 0 such that:
    #   pos_x(t) in {0, s} and pos_y(t) in {0, s}
    #
    # Let's analyze the condition:
    # For pos_x(t):
    #   Let M = 2*s
    #   pos_x(t) = (x + dx*t) mod M
    #   If pos_x(t) > s, pos_x(t) = M - pos_x(t)
    #
    # pos_x(t) = 0 or s means:
    #   Either (x + dx*t) mod M == 0
    #   Or (x + dx*t) mod M == s
    #
    # Similarly for pos_y(t).
    #
    # So we want t > 0 such that:
    #   (x + dx*t) mod M in {0, s}
    #   (y + dy*t) mod M in {0, s}
    #
    # We can try to find t satisfying these congruences.
    #
    # Since dx, dy in {-1, 1}, we can rewrite:
    #   (x + dx*t) mod M = r_x in {0, s}
    #   (y + dy*t) mod M = r_y in {0, s}
    #
    # For each r_x in {0, s}:
    #   t ≡ dx_inv * (r_x - x) mod M
    # For each r_y in {0, s}:
    #   t ≡ dy_inv * (r_y - y) mod M
    #
    # Since dx and dy are ±1, their inverses mod M are themselves (because 1 * 1 = 1 mod M, and -1 * -1 = 1 mod M).
    # So:
    #   t ≡ dx * (r_x - x) mod M
    #   t ≡ dy * (r_y - y) mod M
    #
    # We want to find t that satisfies both congruences simultaneously.
    #
    # Since M = 2*s, and dx, dy = ±1, we can just check all 4 combinations of (r_x, r_y) in {0, s} x {0, s}
    # and see if the congruences have a solution.
    #
    # Because M is the same for both congruences, the solution exists if:
    #   dx*(r_x - x) ≡ dy*(r_y - y) mod M
    #
    # If yes, then t = dx*(r_x - x) mod M is a valid time.
    #
    # We want t > 0, but since the ball moves infinitely, if t=0 is a solution, it means the ball is already at the corner (not possible as per constraints).
    # So t > 0 means t != 0 mod M.
    #
    # If any such t exists, the ball will be potted.

    M = 2 * s
    for r_x in [0, s]:
        for r_y in [0, s]:
            lhs = (dx * (r_x - x)) % M
            rhs = (dy * (r_y - y)) % M
            if lhs == rhs and lhs != 0:
                return True
    return False


def main():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        count = 0
        for __ in range(n):
            dx, dy, x, y = map(int, input().split())
            if will_pot_ball(s, dx, dy, x, y):
                count += 1
        print(count)


if __name__ == "__main__":
    main()