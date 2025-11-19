def max_score(N, K, P):
    NK = N * K
    sorted_P = sorted(P)
    position = {value: idx for idx, value in enumerate(P)}
    score = 0

    for i in range(NK):
        while P[i] != sorted_P[i]:
            target_value = sorted_P[i]
            target_index = position[target_value]

            # Swap P[i] and P[target_index]
            P[i], P[target_index] = P[target_index], P[i]
            position[P[target_index]] = target_index
            position[P[i]] = i

            # Check if the swap is valid for scoring
            if abs(i - target_index) % N == 0:
                score += 1

    return score

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
K = int(data[1])
P = list(map(int, data[2:]))

# Calculate and print the result
print(max_score(N, K, P))