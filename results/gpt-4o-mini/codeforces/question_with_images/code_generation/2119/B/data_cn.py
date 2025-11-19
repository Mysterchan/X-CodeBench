import sys

input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    p_x, p_y, q_x, q_y = map(int, data[index].split())
    index += 1
    a = list(map(int, data[index].split()))
    index += 1

    # Calculate the required distance to reach point q
    required_distance = ((p_x - q_x) ** 2 + (p_y - q_y) ** 2) ** 0.5
    total_distance = sum(a)

    # Check if we can reach the point (q_x, q_y)
    if total_distance >= required_distance and (total_distance - required_distance) % 2 == 0:
        results.append("Yes")
    else:
        results.append("No")

print("\n".join(results))