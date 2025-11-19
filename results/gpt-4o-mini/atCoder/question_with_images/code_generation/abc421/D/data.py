def count_meetings(R_t, C_t, R_a, C_a, N, M, L, S, T):
    # Calculate the total movements for Takahashi
    total_moves_t = [0, 0]  # [vertical, horizontal]
    for direction, count in S:
        if direction == 'U':
            total_moves_t[0] += count
        elif direction == 'D':
            total_moves_t[0] -= count
        elif direction == 'L':
            total_moves_t[1] -= count
        elif direction == 'R':
            total_moves_t[1] += count

    # Calculate the total movements for Aoki
    total_moves_a = [0, 0]  # [vertical, horizontal]
    for direction, count in T:
        if direction == 'U':
            total_moves_a[0] += count
        elif direction == 'D':
            total_moves_a[0] -= count
        elif direction == 'L':
            total_moves_a[1] -= count
        elif direction == 'R':
            total_moves_a[1] += count

    # Calculate the final positions after all moves
    final_t = (R_t + total_moves_t[0], C_t + total_moves_t[1])
    final_a = (R_a + total_moves_a[0], C_a + total_moves_a[1])

    # Calculate the number of meetings
    meetings = 0
    # Check for each move if they meet
    for i in range(N):
        # Calculate current positions
        current_t = (R_t + (total_moves_t[0] * i) // N, C_t + (total_moves_t[1] * i) // N)
        current_a = (R_a + (total_moves_a[0] * i) // N, C_a + (total_moves_a[1] * i) // N)
        
        if current_t == current_a:
            meetings += 1

    return meetings

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

R_t, C_t, R_a, C_a = map(int, data[0].split())
N, M, L = map(int, data[1].split())

S = []
for i in range(2, 2 + M):
    direction, count = data[i].split()
    S.append((direction, int(count)))

T = []
for i in range(2 + M, 2 + M + L):
    direction, count = data[i].split()
    T.append((direction, int(count)))

# Calculate and print the result
print(count_meetings(R_t, C_t, R_a, C_a, N, M, L, S, T))