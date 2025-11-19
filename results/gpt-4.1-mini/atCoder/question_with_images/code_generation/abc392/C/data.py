import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# person i is wearing bib Q[i-1]
# P[i-1] is the person that person i is staring at

# We want for each bib number i (1 to N), find the bib number of the person that the person wearing bib i is staring at.

# Step 1: Create a mapping from bib number to person index
bib_to_person = [0] * (N + 1)
for person in range(1, N + 1):
    bib_to_person[Q[person - 1]] = person

# Step 2: For each bib number i, find the person wearing bib i
# Then find the person they are staring at: P[person - 1]
# Then find the bib number of that person: Q[P[person - 1] - 1]

result = [0] * N
for bib_num in range(1, N + 1):
    person = bib_to_person[bib_num]
    staring_person = P[person - 1]
    result[bib_num - 1] = Q[staring_person - 1]

print(*result)