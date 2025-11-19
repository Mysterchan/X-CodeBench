def solve():
    n, r, c = map(int, input().split())
    s = input()

    # The smoke at time t+0.5 is the set of cells reachable by moving the initial smoke at (0,0)
    # according to the wind directions up to time t.
    # The smoke moves according to the wind, and if (0,0) is empty after moving, new smoke appears at (0,0).
    #
    # Instead of simulating all smoke positions, we track the position of the smoke that started at (0,0) at time 0,
    # and the positions of newly generated smoke at (0,0) at times when the original smoke leaves (0,0).
    #
    # Key insight:
    # The smoke positions at time t+0.5 are the union of all positions:
    #   pos(t) = pos(t-1) moved by s[t]
    #   plus (0,0) if no smoke was at (0,0) after moving at time t.
    #
    # We can track the position of the "oldest" smoke (which moves every step),
    # and keep track of times when new smoke is generated at (0,0).
    #
    # For the query cell (R,C), we want to know at which times t the smoke is at (R,C).
    #
    # The smoke at time t+0.5 includes:
    # - The position of the oldest smoke after t moves.
    # - The positions of all newly generated smoke at (0,0) at times <= t,
    #   which have moved forward (t - generation_time) steps.
    #
    # So, for each time t, the smoke positions are:
    #   {pos_oldest(t)} ∪ {pos_new_smoke(g) moved (t-g) steps | g in generation_times, g ≤ t}
    #
    # We want to check if (R,C) is in this set.
    #
    # To do this efficiently:
    # - Precompute prefix positions of the oldest smoke: pos_oldest[t]
    # - For each generation time g, the new smoke starts at (0,0) at time g,
    #   so its position at time t is pos_oldest[t] - pos_oldest[g]
    #
    # So, (R,C) is in smoke at time t if:
    #   (R,C) == pos_oldest[t]  (oldest smoke)
    # or
    #   (R,C) == pos_oldest[t] - pos_oldest[g] for some g ≤ t (new smoke generated at g)
    #
    # Rearranged:
    #   pos_oldest[g] == pos_oldest[t] - (R,C)
    #
    # We can precompute pos_oldest for all t,
    # and for each t, check if pos_oldest[t] - (R,C) appeared as pos_oldest[g] for some g ≤ t.
    #
    # We can do this by:
    # - Storing positions pos_oldest[t] in a dictionary mapping position -> earliest time it appeared.
    # - For each t, check if pos_oldest[t] - (R,C) is in the dictionary with time ≤ t.
    #
    # Also, we need to know when new smoke is generated:
    #   new smoke generated at time t if pos_oldest[t] != (0,0)
    #   because if after moving, no smoke at (0,0), new smoke appears at (0,0).
    #
    # But since the oldest smoke moves every step, it can leave (0,0).
    # We track this by checking if pos_oldest[t] == (0,0).
    #
    # Implementation details:
    # - pos_oldest[0] = (0,0)
    # - For t in 1..N:
    #     pos_oldest[t] = pos_oldest[t-1] moved by s[t-1]
    # - Keep a dict pos_to_time: position -> earliest time it appeared
    # - For each t:
    #     Check if pos_oldest[t] == (R,C) -> ans[t-1] = '1'
    #     Else check if pos_oldest[t] - (R,C) in pos_to_time with time ≤ t -> ans[t-1] = '1'
    # - Update pos_to_time with pos_oldest[t] if not present
    #
    # This runs in O(N) time.

    move = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    pos_oldest = [(0, 0)]
    for ch in s:
        r0, c0 = pos_oldest[-1]
        dr, dc = move[ch]
        pos_oldest.append((r0 + dr, c0 + dc))

    ans = ['0'] * n
    pos_to_time = dict()
    pos_to_time[(0, 0)] = 0

    for t in range(1, n + 1):
        pr, pc = pos_oldest[t]
        # Check if oldest smoke is at (R,C)
        if (pr, pc) == (r, c):
            ans[t - 1] = '1'
        else:
            # Check if pos_oldest[t] - (R,C) appeared before at time <= t
            key = (pr - r, pc - c)
            if key in pos_to_time and pos_to_time[key] <= t:
                ans[t - 1] = '1'
        # Record earliest time for pos_oldest[t]
        if (pr, pc) not in pos_to_time:
            pos_to_time[(pr, pc)] = t

    print("".join(ans))


if __name__ == "__main__":
    solve()