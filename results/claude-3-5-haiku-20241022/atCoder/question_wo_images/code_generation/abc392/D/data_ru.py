from collections import Counter

n = int(input())
dice = []
for _ in range(n):
    line = list(map(int, input().split()))
    k = line[0]
    faces = line[1:]
    dice.append(faces)

max_prob = 0.0

for i in range(n):
    for j in range(i + 1, n):
        # Вычисляем вероятность того, что кубики i и j покажут одинаковое число
        counter_i = Counter(dice[i])
        counter_j = Counter(dice[j])
        
        prob = 0.0
        for value in counter_i:
            if value in counter_j:
                prob += counter_i[value] * counter_j[value]
        
        prob /= (len(dice[i]) * len(dice[j]))
        max_prob = max(max_prob, prob)

print(max_prob)