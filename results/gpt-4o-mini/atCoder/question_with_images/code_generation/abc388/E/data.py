def max_kagamimochi(n, sizes):
    i, j = 0, 0
    pairs = 0

    while i < n and j < n:
        # Find the first mochi that can be stacked on the ith mochi
        while j < n and sizes[j] < 2 * sizes[i]:
            j += 1
        if j < n:  # A valid mochi found for pairing with sizes[i]
            pairs += 1
            i += 1  # Move to the next mochi to pair
            j += 1  # Move the j index since this mochi is now used
        else:
            break  # No more valid pairings possible

    return pairs

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()

N = int(data[0])
A = list(map(int, data[1:]))

# Calculate maximum K and print it
print(max_kagamimochi(N, A))