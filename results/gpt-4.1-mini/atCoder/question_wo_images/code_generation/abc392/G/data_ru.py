import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
S_set = set(S)

S.sort()

count = 0
for i in range(N):
    for j in range(i+1, N):
        A = S[i]
        B = S[j]
        C = 2*B - A
        if C > S[-1]:
            # Since S is sorted, no need to check further for this i,j
            # but we continue because next j might be larger B
            # Actually, since C depends on B, and B increases with j,
            # C will only increase, so break inner loop
            break
        if C in S_set:
            count += 1

print(count)