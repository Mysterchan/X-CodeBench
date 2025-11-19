import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# Cumulative count of adults with at least one stone at each year
# adults_with_stone[i]: number of adults with stones at year i (1-based)
adults_with_stone = [0] * (N + 1)

# Precompute adults_with_stone
for i in range(N):
    if A[i] > 0:
        adults_with_stone[i + 1] = 1
for i in range(1, N + 1):
    adults_with_stone[i] += adults_with_stone[i - 1]

# Calculate final stones for each alien
# For alien i (0-based), becomes adult at year i+1
# They receive adults_with_stone[i] stones (from adults who became adult before year i+1)
# They give one stone to each new adult after they become adult if they have stones
# So for each alien:
# final = initial - (number of new adults after i+1 who had stones) + (number of adults before i+1 who had stones)
# number of new adults after i+1 who had stones = adults_with_stone[N] - adults_with_stone[i+1]
# number of adults before i+1 who had stones = adults_with_stone[i]

total_adults = adults_with_stone[N]
res = [0] * N
for i in range(N):
    give = total_adults - adults_with_stone[i + 1]
    receive = adults_with_stone[i]
    res[i] = A[i] - give + receive
    if res[i] < 0:
        res[i] = 0

print(' '.join(map(str, res)))