import sys

input = lambda: sys.stdin.readline().rstrip()

def ININ():
    return int(input())

def LIN():
    return list(map(int, input().split()))

N = ININ()

dice = []
for _ in range(N):
    line = LIN()
    K = line[0]
    faces = line[1:]
    
    # Count frequencies using a dictionary
    freq = {}
    for face in faces:
        freq[face] = freq.get(face, 0) + 1
    
    dice.append((K, freq))

max_prob = 0

for i in range(N):
    Ki, freq_i = dice[i]
    for j in range(i + 1, N):
        Kj, freq_j = dice[j]
        
        # Calculate matching count
        match_count = 0
        for value in freq_i:
            if value in freq_j:
                match_count += freq_i[value] * freq_j[value]
        
        prob = match_count / (Ki * Kj)
        max_prob = max(max_prob, prob)

print(max_prob)