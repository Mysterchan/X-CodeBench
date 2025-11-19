def max_intersections(N, chords):
    # Create a list to store the endpoints of the chords
    endpoints = []
    for a, b in chords:
        endpoints.append((min(a, b), max(a, b)))

    # Sort the endpoints based on the first element, and then by the second element
    endpoints.sort()

    # Count the number of intersections
    intersections = 0
    active_chords = []

    for start, end in endpoints:
        # Remove all chords that end before the current start
        active_chords = [e for e in active_chords if e > start]
        # The number of active chords gives the number of intersections with the current chord
        intersections += len(active_chords)
        # Add the current end to the active chords
        active_chords.append(end)

    # The maximum intersections we can achieve is the current intersections + 1
    return intersections + 1

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
chords = [tuple(map(int, line.split())) for line in data[1:N + 1]]

# Get the result and print it
result = max_intersections(N, chords)
print(result)