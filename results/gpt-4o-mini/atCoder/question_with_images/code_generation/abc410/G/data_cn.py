def max_intersections(N, chords):
    # Create a list to store the endpoints of the chords
    endpoints = []
    for a, b in chords:
        endpoints.append((min(a, b), max(a, b)))

    # Sort the chords based on the first endpoint
    endpoints.sort()

    # Use a dynamic programming approach to find the maximum number of intersections
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        dp[i] = dp[i - 1]  # Start with the previous maximum
        for j in range(i):
            if endpoints[j][1] < endpoints[i - 1][0]:  # Non-intersecting condition
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum intersections we can achieve is the maximum of dp array
    return dp[N] + 1  # Adding 1 for the new chord

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
chords = [tuple(map(int, line.split())) for line in data[1:N + 1]]

# Get the result and print it
result = max_intersections(N, chords)
print(result)