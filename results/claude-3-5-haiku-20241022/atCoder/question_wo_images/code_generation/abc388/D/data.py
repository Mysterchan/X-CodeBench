N = int(input())
A = list(map(int, input().split()))

for t in range(N):
    # Alien t+1 (index t) becomes adult at year t+1
    gifts = 0
    # Count gifts from aliens 0 to t-1 (who are already adults)
    for j in range(t):
        if A[j] >= 1:
            A[j] -= 1
            gifts += 1
    A[t] += gifts

print(' '.join(map(str, A)))