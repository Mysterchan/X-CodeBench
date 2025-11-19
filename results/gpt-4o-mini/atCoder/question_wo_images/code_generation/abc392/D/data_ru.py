def max_probability(N, cubes):
    from collections import defaultdict

    max_prob = 0.0

    # Create a dictionary to count occurrences of each number across all cubes
    number_count = defaultdict(int)

    for cube in cubes:
        K = cube[0]
        numbers = cube[1:K + 1]
        for number in numbers:
            number_count[number] += 1

    # Calculate the maximum probability for each pair of cubes
    for i in range(N):
        K1 = cubes[i][0]
        numbers1 = cubes[i][1:K1 + 1]
        count1 = defaultdict(int)
        for number in numbers1:
            count1[number] += 1

        for j in range(i + 1, N):
            K2 = cubes[j][0]
            numbers2 = cubes[j][1:K2 + 1]
            count2 = defaultdict(int)
            for number in numbers2:
                count2[number] += 1

            # Calculate the probability of matching numbers between cube i and cube j
            common_numbers = set(count1.keys()).intersection(set(count2.keys()))
            for number in common_numbers:
                prob = (count1[number] / K1) * (count2[number] / K2)
                max_prob = max(max_prob, prob)

    return max_prob

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
cubes = []

for i in range(1, N + 1):
    line = list(map(int, data[i].split()))
    cubes.append(line)

# Calculate and print the maximum probability
result = max_probability(N, cubes)
print(f"{result:.12f}")