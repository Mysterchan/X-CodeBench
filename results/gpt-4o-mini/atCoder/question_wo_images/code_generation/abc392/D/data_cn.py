def max_probability(N, dice):
    from collections import defaultdict

    # Count occurrences of each number across all dice
    number_count = defaultdict(int)
    for die in dice:
        for number in die[1:]:
            number_count[number] += 1

    max_prob = 0.0

    # Calculate the maximum probability for each pair of dice
    for i in range(N):
        K_i = dice[i][0]
        for number in dice[i][1:]:
            if number in number_count:
                # Probability of getting 'number' from die i
                prob_i = 1 / K_i
                # Probability of getting 'number' from any other die
                for j in range(N):
                    if i != j:
                        K_j = dice[j][0]
                        prob_j = number_count[number] / K_j
                        max_prob = max(max_prob, prob_i * prob_j)

    return max_prob

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
dice = [list(map(int, line.split())) for line in data[1:N+1]]

# Calculate and print the result
result = max_probability(N, dice)
print(f"{result:.12f}")