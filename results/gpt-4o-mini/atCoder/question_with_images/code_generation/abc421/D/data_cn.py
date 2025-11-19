def count_meetings(R_t, C_t, R_a, C_a, N, moves_t, moves_a):
    # Calculate the final position after all moves
    def calculate_final_position(start_r, start_c, moves):
        r, c = start_r, start_c
        for direction, count in moves:
            if direction == 'U':
                r += count
            elif direction == 'D':
                r -= count
            elif direction == 'L':
                c -= count
            elif direction == 'R':
                c += count
        return r, c

    # Calculate the total movements for Takahashi and Aoki
    final_t = calculate_final_position(R_t, C_t, moves_t)
    final_a = calculate_final_position(R_a, C_a, moves_a)

    # Calculate the differences in positions
    delta_r = final_t[0] - final_a[0]
    delta_c = final_t[1] - final_a[1]

    # Count the number of meetings
    meetings = 0
    for i in range(N):
        if delta_r == 0 and delta_c == 0:
            meetings += 1
        # Update positions based on the moves
        if i < len(moves_t):
            direction_t, count_t = moves_t[i]
            if direction_t == 'U':
                delta_r -= count_t
            elif direction_t == 'D':
                delta_r += count_t
            elif direction_t == 'L':
                delta_c += count_t
            elif direction_t == 'R':
                delta_c -= count_t

        if i < len(moves_a):
            direction_a, count_a = moves_a[i]
            if direction_a == 'U':
                delta_r += count_a
            elif direction_a == 'D':
                delta_r -= count_a
            elif direction_a == 'L':
                delta_c -= count_a
            elif direction_a == 'R':
                delta_c += count_a

    return meetings

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

R_t, C_t, R_a, C_a = map(int, data[0].split())
N, M, L = map(int, data[1].split())

moves_t = []
for i in range(2, 2 + M):
    direction, count = data[i].split()
    moves_t.append((direction, int(count)))

moves_a = []
for i in range(2 + M, 2 + M + L):
    direction, count = data[i].split()
    moves_a.append((direction, int(count)))

# Calculate and print the result
result = count_meetings(R_t, C_t, R_a, C_a, N, moves_t, moves_a)
print(result)