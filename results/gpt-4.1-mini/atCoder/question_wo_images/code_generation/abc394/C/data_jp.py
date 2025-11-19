S = list(input())
i = 0
while i < len(S) - 1:
    if S[i] == 'W' and S[i+1] == 'A':
        S[i], S[i+1] = 'A', 'C'
        i = max(i - 1, 0)
    else:
        i += 1
print(''.join(S))