from collections import Counter

N = int(input())
dice = []
for _ in range(N):
    line = list(map(int, input().split()))
    K = line[0]
    faces = line[1:K+1]
    dice.append(faces)

max_prob = 0.0

for i in range(N):
    for j in range(i+1, N):
        # Calculate probability that dice i and dice j show the same value
        counter_i = Counter(dice[i])
        counter_j = Counter(dice[j])
        
        K_i = len(dice[i])
        K_j = len(dice[j])
        
        prob = 0.0
        for value in counter_i:
            if value in counter_j:
                prob += (counter_i[value] / K_i) * (counter_j[value] / K_j)
        
        max_prob = max(max_prob, prob)

print(max_prob)