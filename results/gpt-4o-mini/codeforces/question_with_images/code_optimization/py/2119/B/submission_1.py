t = int(input())
results = []
for _ in range(t):
    n = int(input())
    px, py, qx, qy = map(int, input().split())
    distances = list(map(int, input().split()))
    
    # Calculate the required distance from p to q
    required_distance = ((px - qx) ** 2 + (py - qy) ** 2) ** 0.5
    sum_distances = sum(distances)

    # Check the two conditions
    if (required_distance <= sum_distances and
        (sum_distances - required_distance) % 2 == 0):
        results.append("Yes")
    else:
        results.append("No")

# Print all results at once
print("\n".join(results))