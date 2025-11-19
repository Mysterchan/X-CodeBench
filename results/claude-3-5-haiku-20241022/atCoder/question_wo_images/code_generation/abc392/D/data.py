from collections import Counter

n = int(input())
dice = []

for _ in range(n):
    line = list(map(int, input().split()))
    k = line[0]
    faces = line[1:k+1]
    dice.append(faces)

max_prob = 0.0

for i in range(n):
    for j in range(i+1, n):
        # Count occurrences of each value on each die
        count_i = Counter(dice[i])
        count_j = Counter(dice[j])
        
        k_i = len(dice[i])
        k_j = len(dice[j])
        
        # Calculate probability of getting the same number
        prob = 0.0
        for value in count_i:
            if value in count_j:
                prob += (count_i[value] / k_i) * (count_j[value] / k_j)
        
        max_prob = max(max_prob, prob)

print(max_prob)