S = input()
n = len(S)
count = 0

for j in range(n):
    if S[j] == 'B':
        for d in range(1, n):
            i = j - d
            k = j + d
            if i >= 0 and k < n:
                if S[i] == 'A' and S[k] == 'C':
                    count += 1

print(count)