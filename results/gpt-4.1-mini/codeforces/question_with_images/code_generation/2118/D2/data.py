import sys
import bisect

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    d = list(map(int, input().split()))
    q = int(input())
    a = list(map(int, input().split()))

    # Precompute for each traffic light:
    # The times when it is red are t such that t % k == d_i
    # At time t, if you are at position p_i and t % k == d_i, you turn around.

    # The movement:
    # At second t:
    # 1) If current cell has red light at time t, turn around
    # 2) Move one cell in current direction

    # We want to know if starting at position a_i at time 0 facing right,
    # will we eventually leave the strip [1, 10^15] within 10^100 seconds.

    # Key observations:
    # - The strip is from 1 to 10^15.
    # - The traffic lights are at positions p_1 < p_2 < ... < p_n.
    # - Outside the traffic lights, no red lights, so no turning.
    # - Turning only happens at traffic lights when time % k == d_i.
    # - The time modulo k cycles every k seconds.
    # - The problem is large, so we cannot simulate.

    # Approach:
    # The movement is deterministic and periodic modulo k.
    # The position and direction at time t depends on the initial position and the sequence of red lights encountered.

    # We want to find if the person will eventually leave the strip.
    # Leaving means position < 1 or position > 10^15.

    # Since the strip is huge, and the number of traffic lights is up to 2*10^5,
    # we can consider the traffic lights as "checkpoints".

    # The person moves step by step, turning only at red lights at specific times.

    # Let's analyze the movement in terms of intervals between traffic lights.

    # The person starts at position a_i, facing right.

    # If the person starts outside the traffic lights (less than p[0] or greater than p[-1]),
    # then no traffic lights ahead in that direction, so no turning, so will leave strip eventually.

    # If the person starts exactly at a traffic light, then at time 0:
    # if t=0 % k == d_i, turn around immediately, else move forward.

    # The main difficulty is to determine if the person gets trapped between two traffic lights forever.

    # Let's define:
    # For each traffic light i, define the set of times when it is red: t % k == d_i.

    # The person moves from one traffic light to another, possibly turning at red lights.

    # The key is to find if the person can get stuck in a cycle between two traffic lights.

    # Let's consider the intervals between traffic lights:
    # [1, p_0), (p_0, p_1), ..., (p_{n-2}, p_{n-1}), (p_{n-1}, 10^15]

    # If the person is in an interval with no traffic lights, he moves straight until he leaves the strip.

    # So the only way to get stuck is between two traffic lights.

    # Let's analyze the behavior at traffic lights:

    # At traffic light at position p_i:
    # At time t, if t % k == d_i, turn around, else continue.

    # The person moves one cell per second.

    # Let's consider the time modulo k when the person arrives at a traffic light.

    # The time modulo k when the person arrives at p_i depends on the starting time modulo k and the distance traveled.

    # Since the person starts at time 0, the time modulo k at position x is (distance traveled) % k.

    # The distance traveled is abs(x - a_i).

    # So the time modulo k at position p_i is (abs(p_i - a_i)) % k.

    # If this equals d_i, the person turns around at p_i.

    # So the turning condition at p_i is:
    # (abs(p_i - a_i)) % k == d_i

    # This is the key to determine if the person turns at p_i.

    # Now, the person moves in a direction until hitting a traffic light where he turns around.

    # So the movement is a sequence of moves between traffic lights, turning at some of them.

    # The person can get stuck if he bounces between two traffic lights forever.

    # So we need to check if there exists a pair of traffic lights between which the person bounces forever.

    # Let's define for each traffic light i:
    # The turning condition: (abs(p_i - a_i)) % k == d_i

    # For the person starting at a_i facing right:

    # We can simulate the bouncing between traffic lights by checking the turning conditions at the lights.

    # But we cannot simulate for each query.

    # Instead, we can precompute for each traffic light the set of positions from which the person would turn at that light.

    # But that is too large.

    # Alternative approach:

    # For each query a_i:

    # 1) Find the closest traffic light to the left and right of a_i.

    # 2) Check if the person turns at these traffic lights.

    # 3) If the person does not turn at any traffic light in the direction he moves, he will leave the strip.

    # 4) If the person turns at a traffic light, he reverses direction.

    # 5) If the person bounces between two traffic lights forever, answer NO.

    # 6) Otherwise, YES.

    # Let's implement this logic:

    # For each query a_i:

    # - Determine initial direction: right

    # - current position = a_i

    # - We will simulate the bouncing between traffic lights by checking turning conditions at the lights.

    # Since the person moves one cell per second, the time modulo k at position x is (abs(x - a_i)) % k.

    # We can simulate the bouncing between traffic lights by moving from one traffic light to another, checking turning conditions.

    # Since the number of traffic lights is large, we cannot simulate many steps.

    # But the bouncing can only happen between two traffic lights.

    # So the person can be trapped only if he bounces between two traffic lights.

    # So we check if the person turns at both traffic lights bounding the interval where he is trapped.

    # If yes, then NO.

    # Otherwise, YES.

    # Let's implement this:

    # For each query:

    # 1) Find the index of the closest traffic light to the left (idx_left) and right (idx_right) of a_i.

    # 2) If a_i < p[0], no traffic light to the left, so the person moves right and leaves strip eventually => YES.

    # 3) If a_i > p[-1], no traffic light to the right, so the person moves right and leaves strip eventually => YES.

    # 4) Otherwise, the person is between p[idx_left] and p[idx_right].

    # 5) Check turning conditions at p[idx_left] and p[idx_right]:

    #    - turn_left = ((a_i - p[idx_left]) % k) == d[idx_left]

    #    - turn_right = ((p[idx_right] - a_i) % k) == d[idx_right]

    # 6) If both turn_left and turn_right are True, the person bounces forever => NO.

    # 7) Else YES.

    # Edge cases:

    # - If a_i == p[i], then the person is at a traffic light.

    #   At time 0, time modulo k = 0.

    #   So turning condition is (abs(p[i] - a_i)) % k == d[i] => 0 == d[i].

    #   If d[i] == 0, turn around immediately.

    #   So the person reverses direction at start.

    #   We can handle this by the same logic.

    # Let's implement this now.

    # Preprocessing done, now answer queries.

    for pos in a:
        # Find right traffic light index >= pos
        idx_right = bisect.bisect_left(p, pos)
        idx_left = idx_right - 1

        # If no traffic light to the right
        if idx_right == n:
            # Person moves right and leaves strip eventually
            print("YES")
            continue
        # If no traffic light to the left
        if idx_left == -1:
            # Person moves right and leaves strip eventually
            print("YES")
            continue

        # Check turning conditions
        turn_left = ((pos - p[idx_left]) % k) == d[idx_left]
        turn_right = ((p[idx_right] - pos) % k) == d[idx_right]

        if turn_left and turn_right:
            print("NO")
        else:
            print("YES")