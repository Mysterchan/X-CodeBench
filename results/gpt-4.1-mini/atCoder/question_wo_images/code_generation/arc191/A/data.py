import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(input().strip())
T = list(input().strip())

# Sort T in descending order to use the largest digits first
T.sort(reverse=True)

j = 0  # pointer for T
for i in range(N):
    if j < M and T[j] > S[i]:
        S[i] = T[j]
        j += 1
    if j == M:
        break

print("".join(S))