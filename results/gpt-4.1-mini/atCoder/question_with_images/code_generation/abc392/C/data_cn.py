import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# P[i] = the person that person i+1 is looking at
# Q[i] = the apron number of person i+1

# We want for each apron number i (1 to N), find the apron number of the person they are looking at.

# Step 1: Build a mapping from person number to apron number
person_to_apron = Q  # index i corresponds to person i+1

# Step 2: Build a mapping from apron number to person number
apron_to_person = [0]*(N+1)
for i, apron in enumerate(Q, 1):
    apron_to_person[apron] = i

# Step 3: For each apron number i, find the person wearing apron i
# Then find the person they are looking at: P[person-1]
# Then find the apron number of that person

res = [0]*N
for apron_num in range(1, N+1):
    person = apron_to_person[apron_num]
    looked_person = P[person-1]
    res[apron_num-1] = person_to_apron[looked_person-1]

print(' '.join(map(str, res)))