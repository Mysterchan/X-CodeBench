def max_probability(N, dice):
    from collections import defaultdict

    max_prob = 0.0

    # Iterate through all pairs of dice
    for i in range(N):
        for j in range(i + 1, N):
            # Count occurrences of each face in both dice
            count_i = defaultdict(int)
            count_j = defaultdict(int)

            for face in dice[i][1:]:
                count_i[face] += 1
            
            for face in dice[j][1:]:
                count_j[face] += 1
            
            # Calculate the probability of matching faces
            total_prob = 0.0
            for face in count_i:
                if face in count_j:
                    total_prob += (count_i[face] / (len(dice[i]) - 1)) * (count_j[face] / (len(dice[j]) - 1))
            
            max_prob = max(max_prob, total_prob)

    return max_prob

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
dice = [list(map(int, line.split())) for line in data[1:N + 1]]

# Calculate and print the maximum probability
result = max_probability(N, dice)
print(f"{result:.12f}")