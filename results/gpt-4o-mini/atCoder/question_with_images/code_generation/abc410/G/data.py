def max_intersections(N, chords):
    # Sort chords based on the first point of each chord
    chords.sort(key=lambda x: (min(x), max(x)))

    # Create a list to store the second points of the chords
    second_points = [0] * N
    for i in range(N):
        second_points[i] = max(chords[i])

    # Count the number of intersections
    intersections = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (min(chords[i]) < min(chords[j]) < max(chords[i]) < max(chords[j])) or \
               (min(chords[j]) < min(chords[i]) < max(chords[j]) < max(chords[i]))):
                intersections += 1

    # The maximum possible intersections after adding one chord
    return intersections + 1

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
chords = [tuple(map(int, line.split())) for line in data[1:N + 1]]

# Output the result
print(max_intersections(N, chords))