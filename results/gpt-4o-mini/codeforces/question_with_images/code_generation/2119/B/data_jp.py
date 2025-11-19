import sys

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    px, py, qx, qy = map(int, data[index:index+4])
    index += 4
    a = list(map(int, data[index:index+n]))
    index += n
    
    # calculate the required distance to reach q
    target_distance = ((qx - px) ** 2 + (qy - py) ** 2) ** 0.5
    total_distance = sum(a)
    
    # check if we can reach the target point
    if total_distance >= target_distance and (total_distance - target_distance) % 2 == 0:
        results.append("Yes")
    else:
        results.append("No")

print("\n".join(results))