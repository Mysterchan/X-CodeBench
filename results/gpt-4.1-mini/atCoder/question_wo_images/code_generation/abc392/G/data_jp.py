import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
S_set = set(S)

S.sort()
count = 0

for i in range(N):
    for j in range(i+1, N):
        diff = S[j] - S[i]
        c = S[j] + diff
        if c > 10**6:
            break
        if c in S_set:
            count += 1

print(count)