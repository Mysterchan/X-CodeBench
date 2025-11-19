from collections import Counter

n = int(input())
dices = []
for _ in range(n):
    line = list(map(int, input().split()))
    k = line[0]
    faces = line[1:k+1]
    dices.append(faces)

max_prob = 0.0

for i in range(n):
    for j in range(i+1, n):
        # 计算骰子i和j显示相同数字的概率
        counter_i = Counter(dices[i])
        counter_j = Counter(dices[j])
        
        # 找到两个骰子共同拥有的数字
        common_numbers = set(counter_i.keys()) & set(counter_j.keys())
        
        prob = 0.0
        for num in common_numbers:
            # 该数字在两个骰子上同时出现的概率
            prob += (counter_i[num] / len(dices[i])) * (counter_j[num] / len(dices[j]))
        
        max_prob = max(max_prob, prob)

print(max_prob)