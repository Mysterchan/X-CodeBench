import sys
import math

input = sys.stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    p_x, p_y, q_x, q_y = map(int, data[index].split())
    index += 1
    a = list(map(int, data[index].split()))
    index += 1

    total_distance = sum(a)
    euclidean_distance = math.sqrt((p_x - q_x) ** 2 + (p_y - q_y) ** 2)

    # Check if the final point can be reached
    if (total_distance >= euclidean_distance) and ((total_distance - euclidean_distance) % 2 == 0):
        results.append("Yes")
    else:
        results.append("No")

# Print all results at once
print("\n".join(results))