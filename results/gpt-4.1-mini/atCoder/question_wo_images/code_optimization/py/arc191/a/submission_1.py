N, M = map(int, input().split())
S = list(map(int, input()))
T = list(map(int, input()))

# Sort T in descending order to use the largest digits first
T.sort(reverse=True)

idx = 0
for t_digit in T:
    if idx < N and S[idx] < t_digit:
        S[idx] = t_digit
        idx += 1
    else:
        # If current S[idx] >= t_digit, move to next S[idx]
        # but since T is sorted descending, no need to try further if S[idx] >= t_digit
        # because next t_digit will be smaller or equal
        # So we only increment idx if we replaced a digit
        # Otherwise, just continue to next t_digit without incrementing idx
        # But since we want to replace only if t_digit > S[idx], we skip replacement
        # and move to next t_digit
        pass

print(''.join(map(str, S)))