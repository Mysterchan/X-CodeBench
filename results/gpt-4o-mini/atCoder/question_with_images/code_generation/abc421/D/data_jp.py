def count_meetings(R_t, C_t, R_a, C_a, N, S, T):
    # Initialize positions
    pos_t = (R_t, C_t)
    pos_a = (R_a, C_a)
    
    # Movement deltas
    move_map = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    
    # Count of meetings
    meeting_count = 0
    
    # Process S
    s_index = 0
    for direction, count in S:
        for _ in range(count):
            # Move Takahashi
            delta_t = move_map[direction]
            pos_t = (pos_t[0] + delta_t[0], pos_t[1] + delta_t[1])
            
            # Move Aoki
            if s_index < len(T):
                direction_a, count_a = T[s_index]
                delta_a = move_map[direction_a]
                pos_a = (pos_a[0] + delta_a[0], pos_a[1] + delta_a[1])
                
                # Check if they meet
                if pos_t == pos_a:
                    meeting_count += 1
            
            # Increment index for Aoki's movements
            if s_index < len(T) and count_a > 1:
                T[s_index] = (direction_a, count_a - 1)
            else:
                s_index += 1
    
    return meeting_count

import sys
input = sys.stdin.read
data = input().splitlines()

# Read initial positions
R_t, C_t, R_a, C_a = map(int, data[0].split())
# Read N, M, L
N, M, L = map(int, data[1].split())

# Read S
S = []
for i in range(2, 2 + M):
    direction, count = data[i].split()
    S.append((direction, int(count)))

# Read T
T = []
for i in range(2 + M, 2 + M + L):
    direction, count = data[i].split()
    T.append((direction, int(count)))

# Count meetings
result = count_meetings(R_t, C_t, R_a, C_a, N, S, T)
print(result)