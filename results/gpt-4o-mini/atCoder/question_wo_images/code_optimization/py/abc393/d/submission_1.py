N = int(input())
S = input()

# Find the positions of all '1's in the string
positions = [i for i in range(N) if S[i] == '1']
count1 = len(positions)

# If all 1s are already contiguous, no swaps are needed
if count1 == 0 or count1 == N:
    print(0)
    exit()

# Calculate the minimum number of swaps needed
# The target positions for the 1s to be contiguous
target_positions = range(positions[0], positions[0] + count1)

# Calculate the number of swaps needed to move each '1' to its target position
swaps = sum(abs(positions[i] - target_positions[i]) for i in range(count1))

print(swaps)