def smoke_in_grid(N, R, C, S):
    smoke_positions = {(0, 0)}
    result = []

    for t in range(N):
        direction = S[t]
        new_smoke_positions = set()

        for r, c in smoke_positions:
            if direction == 'N':
                new_smoke_positions.add((r - 1, c))
            elif direction == 'W':
                new_smoke_positions.add((r, c - 1))
            elif direction == 'S':
                new_smoke_positions.add((r + 1, c))
            elif direction == 'E':
                new_smoke_positions.add((r, c + 1))

        smoke_positions = new_smoke_positions

        if (0, 0) not in smoke_positions:
            smoke_positions.add((0, 0))

        if (R, C) in smoke_positions:
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)

# Read input
N, R, C = map(int, input().split())
S = input().strip()

# Get the result and print it
print(smoke_in_grid(N, R, C, S))