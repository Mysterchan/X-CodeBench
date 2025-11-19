def solve(N, C):
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + (1 if C[i] > 0 else 0)

    result = [0] * N
    for i in range(N):
        # Number of adults before i-th alien becomes adult
        adults_before = prefix[i]
        # Stones given to i-th alien
        result[i] = C[i] + adults_before

    # Calculate how many stones each alien loses
    # Each alien loses one stone for each alien that becomes adult after them,
    # but only if they have stones at that time.
    # The number of aliens that become adult after i-th alien is (N - i - 1)
    # But they only lose stones if they have stones at that time.
    # Since stones decrease by 1 each time they give a stone, the max stones lost is min(C[i], N - i - 1)
    for i in range(N):
        lost = min(C[i], N - i - 1)
        result[i] -= lost

    return " ".join(map(str, result))

N = int(input())
C = list(map(int, input().split()))
print(solve(N, C))