def can_transform(N, X, Y, S, T):
    # Convert strings to lists for easier manipulation
    S = list(S)
    T = list(T)

    # We will track the number of 0s and 1s that need to be changed
    count_0_to_1 = 0
    count_1_to_0 = 0

    # We will iterate through the strings and count the differences
    for i in range(N):
        if S[i] != T[i]:
            if T[i] == '1':
                count_0_to_1 += 1
            else:
                count_1_to_0 += 1

    # We can only change blocks of size X and Y
    # We need to check if we can balance the counts of 0s and 1s
    # The number of 1s we need to create must be less than or equal to the number of 0s we can change
    # and vice versa
    if count_0_to_1 > (N // (X + Y)) * Y or count_1_to_0 > (N // (X + Y)) * X:
        return "No"

    # If we can balance the counts, we can transform S into T
    return "Yes"

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, X, Y = map(int, data[0].split())
S = data[1].strip()
T = data[2].strip()

# Get the result and print it
result = can_transform(N, X, Y, S, T)
print(result)