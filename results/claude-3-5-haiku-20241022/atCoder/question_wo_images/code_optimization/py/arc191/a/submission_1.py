N, M = map(int, input().split())
S = list(input())
T = input()

# Build position lists for each digit in T (from right to left)
digit_positions = [[] for _ in range(10)]
for i in range(M - 1, -1, -1):
    digit_positions[int(T[i])].append(i)

# Greedily replace positions in S from left to right
s_idx = 0
min_s = 10
min_t_pos = M

# Process digits from 9 down to 0
for digit in range(9, -1, -1):
    positions = digit_positions[digit]
    
    for t_pos in positions:
        # Skip positions in S that already have a digit >= current digit
        while s_idx < N and int(S[s_idx]) >= digit:
            min_s = min(min_s, int(S[s_idx]))
            s_idx += 1
        
        # If we can still replace in S, do it
        if s_idx < N:
            S[s_idx] = str(digit)
            min_s = min(min_s, digit)
            s_idx += 1
            min_t_pos = min(min_t_pos, t_pos)

# If there are unused operations and the last char of S can be improved
if min_t_pos >= 1:
    last_t = int(T[-1])
    if min_s > last_t:
        S[-1] = str(last_t)

print(''.join(S))