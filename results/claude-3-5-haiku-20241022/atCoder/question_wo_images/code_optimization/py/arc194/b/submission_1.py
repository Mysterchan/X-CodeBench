N = int(input())
P = list(map(int, input().split()))

ans = 0
for i in range(N):
    # Find where element i+1 currently is (0-indexed positions, 1-indexed values)
    pos = P.index(i + 1)
    # Move it to position i
    while pos > i:
        # Swap at position pos-1 (0-indexed), which costs pos (1-indexed)
        ans += pos
        P[pos - 1], P[pos] = P[pos], P[pos - 1]
        pos -= 1

print(ans)