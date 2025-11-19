def max_intersections(N, chords):
    # Sort chords based on the minimum of the two points
    chords = [(min(a, b), max(a, b)) for a, b in chords]
    chords.sort()

    # Count the number of non-crossing chords
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1]
        for j in range(i):
            if chords[j][1] < chords[i - 1][0]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum number of intersections we can achieve
    max_non_crossing = dp[N]
    max_intersections = max_non_crossing + 1  # Adding one new chord

    return max_intersections

import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
chords = [tuple(map(int, line.split())) for line in data[1:N + 1]]

print(max_intersections(N, chords))