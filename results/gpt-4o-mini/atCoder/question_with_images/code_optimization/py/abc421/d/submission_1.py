Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())
S = []
T = []

for _ in range(M):
    direction, count = input().split()
    S.append((direction, int(count)))

for _ in range(L):
    direction, count = input().split()
    T.append((direction, int(count)))

def compute_final_positions(sequence):
    x, y = 0, 0
    for direction, count in sequence:
        if direction == 'U':
            x -= count
        elif direction == 'D':
            x += count
        elif direction == 'L':
            y -= count
        elif direction == 'R':
            y += count
    return x, y

# Compute net movements for Takahashi and Aoki
final_takahashi = compute_final_positions(S)
final_aoki = compute_final_positions(T)

# Calculate the number of times they meet
count = 0
T_x, T_y = Rt, Ct
A_x, A_y = Ra, Ca

# We generate the complete paths, but only on-the-fly for counting meetings
total_moves_t = []
total_moves_a = []

# Create movement counts for Takahashi
for direction, count in S:
    total_moves_t.append((direction, count))

# Create movement counts for Aoki
for direction, count in T:
    total_moves_a.append((direction, count))

# Initialize indices
t_index = 0
a_index = 0
t_move_remaining = total_moves_t[t_index][1] if total_moves_t else 0
a_move_remaining = total_moves_a[a_index][1] if total_moves_a else 0

for i in range(N):
    # Move Takahashi if he still has moves left
    if t_move_remaining > 0:
        if total_moves_t[t_index][0] == 'U':
            T_x -= 1
        elif total_moves_t[t_index][0] == 'D':
            T_x += 1
        elif total_moves_t[t_index][0] == 'L':
            T_y -= 1
        elif total_moves_t[t_index][0] == 'R':
            T_y += 1
        
        t_move_remaining -= 1
        
        if t_move_remaining == 0:
            t_index += 1
            if t_index < len(total_moves_t):
                t_move_remaining = total_moves_t[t_index][1]

    # Move Aoki if he still has moves left
    if a_move_remaining > 0:
        if total_moves_a[a_index][0] == 'U':
            A_x -= 1
        elif total_moves_a[a_index][0] == 'D':
            A_x += 1
        elif total_moves_a[a_index][0] == 'L':
            A_y -= 1
        elif total_moves_a[a_index][0] == 'R':
            A_y += 1
            
        a_move_remaining -= 1
        
        if a_move_remaining == 0:
            a_index += 1
            if a_index < len(total_moves_a):
                a_move_remaining = total_moves_a[a_index][1]

    # Check if they meet
    if T_x == A_x and T_y == A_y:
        count += 1

print(count)