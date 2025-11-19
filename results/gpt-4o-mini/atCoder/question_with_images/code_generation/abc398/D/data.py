def smoke_at_time(N, R, C, S):
    # Initialize the smoke positions
    smoke_positions = {(0, 0)}
    result = []

    # Direction vectors for N, W, S, E
    direction = {
        'N': (-1, 0),
        'W': (0, -1),
        'S': (1, 0),
        'E': (0, 1)
    }

    for t in range(N):
        # Check if smoke exists at (R, C) at time t + 0.5
        if (R, C) in smoke_positions:
            result.append('1')
        else:
            result.append('0')

        # Move the smoke according to the wind direction
        new_smoke_positions = set()
        for r, c in smoke_positions:
            # Move smoke
            dr, dc = direction[S[t]]
            new_smoke_positions.add((r + dr, c + dc))

        # If no smoke exists at (0, 0), generate new smoke
        if (0, 0) not in smoke_positions:
            new_smoke_positions.add((0, 0))

        # Update smoke positions
        smoke_positions = new_smoke_positions

    # Check for the last time point
    if (R, C) in smoke_positions:
        result.append('1')
    else:
        result.append('0')

    return ''.join(result)

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
N, R, C = map(int, data[0].split())
S = data[1]

# Get the result and print it
print(smoke_at_time(N, R, C, S))