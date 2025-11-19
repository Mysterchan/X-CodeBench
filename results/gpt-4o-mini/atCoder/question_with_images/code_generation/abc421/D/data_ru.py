def count_meetings(R_t, C_t, R_a, C_a, N, S, T):
    # Calculate the total movements for Takahashi and Aoki
    delta_t = [0, 0]  # [vertical, horizontal]
    delta_a = [0, 0]  # [vertical, horizontal]

    # Process Takahashi's movements
    for move in S:
        if move == 'U':
            delta_t[0] += 1
        elif move == 'D':
            delta_t[0] -= 1
        elif move == 'L':
            delta_t[1] -= 1
        elif move == 'R':
            delta_t[1] += 1

    # Process Aoki's movements
    for move in T:
        if move == 'U':
            delta_a[0] += 1
        elif move == 'D':
            delta_a[0] -= 1
        elif move == 'L':
            delta_a[1] -= 1
        elif move == 'R':
            delta_a[1] += 1

    # Calculate the final positions after all moves
    final_t = (R_t + delta_t[0], C_t + delta_t[1])
    final_a = (R_a + delta_a[0], C_a + delta_a[1])

    # Count the number of meetings
    meetings = 0
    for i in range(N):
        if (R_t, C_t) == (R_a, C_a):
            meetings += 1
        
        # Update positions for the next move
        if i < len(S):
            if S[i] == 'U':
                R_t -= 1
            elif S[i] == 'D':
                R_t += 1
            elif S[i] == 'L':
                C_t -= 1
            elif S[i] == 'R':
                C_t += 1
        
        if i < len(T):
            if T[i] == 'U':
                R_a -= 1
            elif T[i] == 'D':
                R_a += 1
            elif T[i] == 'L':
                C_a -= 1
            elif T[i] == 'R':
                C_a += 1

    return meetings

import sys
input = sys.stdin.read
data = input().splitlines()

# Read initial positions
R_t, C_t, R_a, C_a = map(int, data[0].split())
# Read N, M, L
N, M, L = map(int, data[1].split())

# Read Takahashi's movements
S = []
for i in range(2, 2 + M):
    move, count = data[i].split()
    S.append(move * int(count))

# Read Aoki's movements
T = []
for i in range(2 + M, 2 + M + L):
    move, count = data[i].split()
    T.append(move * int(count))

# Concatenate movements
S = ''.join(S)
T = ''.join(T)

# Get the result
result = count_meetings(R_t, C_t, R_a, C_a, N, S, T)
print(result)