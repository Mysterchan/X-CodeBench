import sys
input = sys.stdin.readline

N = int(input())
dice = []
for _ in range(N):
    data = list(map(int, input().split()))
    K = data[0]
    faces = data[1:]
    freq = {}
    for f in faces:
        freq[f] = freq.get(f, 0) + 1
    dice.append((K, freq))

max_prob = 0.0

for i in range(N):
    K_i, freq_i = dice[i]
    for j in range(i+1, N):
        K_j, freq_j = dice[j]
        # Calculate probability that two dice show the same number
        # sum over all numbers that appear in both dice:
        # (freq_i[num]/K_i) * (freq_j[num]/K_j)
        prob = 0.0
        # Iterate over smaller freq dict for efficiency
        if len(freq_i) < len(freq_j):
            for num, count_i in freq_i.items():
                count_j = freq_j.get(num, 0)
                if count_j > 0:
                    prob += (count_i / K_i) * (count_j / K_j)
        else:
            for num, count_j in freq_j.items():
                count_i = freq_i.get(num, 0)
                if count_i > 0:
                    prob += (count_i / K_i) * (count_j / K_j)
        if prob > max_prob:
            max_prob = prob

print(max_prob)