N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Create a mapping of bib numbers to their indices
bib_to_index = {Q[i]: i for i in range(N)}

# Prepare the result list
result = [0] * N

# For each person i (1-based index):
for i in range(1, N + 1):
    person_staring_at = P[bib_to_index[i]]  # Find who is i staring at
    result[i - 1] = Q[person_staring_at - 1]  # Get the bib number of that person

# Print the result
print(" ".join(map(str, result)))