N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Create a mapping from bib number to person index
bib_to_person = [0] * (N + 1)
for i in range(N):
    bib_to_person[Q[i]] = i

# For each bib number i, find the person they are staring at and print that person's bib number
result = [0] * N
for i in range(1, N + 1):
    person_index = bib_to_person[i]
    staring_person = P[person_index] - 1
    result[i - 1] = Q[staring_person]

print(*result)