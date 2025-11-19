import sys
input = sys.stdin.readline

N, R, C = map(int, input().split())
S = input().strip()

# We want to know if smoke exists at (R,C) at time t+0.5 for t=1..N.

# Key insight:
# At time t+0.5, smoke cells are the union of:
# - The smoke cells at time t-0.5 moved by the wind at time t
# - Plus possibly new smoke at (0,0) if no smoke was there at time t-0.5

# Instead of simulating smoke forward, simulate backward from (R,C) at time t+0.5:
# For smoke to be at (R,C) at time t+0.5, it must have been at the cell that moves to (R,C) at time t-0.5,
# or (if (0,0) is empty at time t-0.5) new smoke is generated at (0,0).

# We track a set of possible positions where smoke could have been at time t-0.5 to reach (R,C) at time t+0.5.
# Initially at time N+0.5, the set is {(R,C)}.
# We move backward from t=N down to 1, updating the set of possible positions at time t-0.5.

# If at any time (0,0) is not in the set, new smoke is generated at (0,0) at time t-0.5,
# so we add (0,0) to the set.

# After processing time t, if (R,C) is in the set at time t+0.5, output '1', else '0'.

# To do this efficiently, we represent the set as a boolean array over the range [-N..N] for rows and columns.
# Since N can be up to 200000, a full 2D array is too large.
# Instead, we use a set of positions.

# But sets can be large. However, the smoke can only spread at most t steps away from (0,0),
# so the number of positions is at most O(t), which is manageable.

# We'll implement the backward simulation with sets.

# Direction mapping for backward movement:
# At time t, wind blows in direction S[t-1].
# Forward movement:
# N: (r,c) -> (r-1,c)
# W: (r,c) -> (r,c-1)
# S: (r,c) -> (r+1,c)
# E: (r,c) -> (r,c+1)
# Backward movement (to find previous positions):
# N: (r,c) at t+0.5 comes from (r+1,c) at t-0.5
# W: (r,c) at t+0.5 comes from (r,c+1) at t-0.5
# S: (r,c) at t+0.5 comes from (r-1,c) at t-0.5
# E: (r,c) at t+0.5 comes from (r,c-1) at t-0.5

# We'll process from t=N down to 1.

# Initialize current positions at time N+0.5:
cur = {(R,C)}

res = ['0'] * N

for t in range(N, 0, -1):
    # Check if (R,C) is in cur at time t+0.5
    if (R,C) in cur:
        res[t-1] = '1'
    else:
        res[t-1] = '0'

    # Backward move: find positions at time t-0.5 that move to cur at time t+0.5
    d = S[t-1]
    prev = set()
    if d == 'N':
        # backward: (r,c) at t+0.5 comes from (r+1,c)
        for r,c in cur:
            prev.add((r+1,c))
    elif d == 'W':
        # backward: (r,c) at t+0.5 comes from (r,c+1)
        for r,c in cur:
            prev.add((r,c+1))
    elif d == 'S':
        # backward: (r,c) at t+0.5 comes from (r-1,c)
        for r,c in cur:
            prev.add((r-1,c))
    else: # 'E'
        # backward: (r,c) at t+0.5 comes from (r,c-1)
        for r,c in cur:
            prev.add((r,c-1))

    # If (0,0) not in prev, new smoke generated at (0,0)
    if (0,0) not in prev:
        prev.add((0,0))

    cur = prev

print(''.join(res))