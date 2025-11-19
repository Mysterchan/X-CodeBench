N, M = map(int, input().split())
S = list(input().strip())
T = input().strip()

for k in range(M):
    t_char = T[k]
    
    # Find the leftmost position where t_char > S[i]
    best_pos = -1
    for i in range(N):
        if t_char > S[i]:
            best_pos = i
            break
    
    # If we found a position to improve, replace it
    if best_pos != -1:
        S[best_pos] = t_char
    else:
        # If no improvement possible, replace the last position
        # (least significant digit to minimize negative impact)
        S[N-1] = t_char

print(''.join(S))