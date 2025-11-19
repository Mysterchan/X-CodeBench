N, L = map(int, input().split())
d = list(map(int, input().split()))
positions = [0] * N

# Calculate the positions of the points on the circle
for i in range(1, N):
    positions[i] = (positions[i - 1] + d[i - 1]) % L

# Sort the positions
positions.sort()

# Use a dictionary to store count of valid arrangements
ans = 0
count_map = {}

# Iterate through each position and count valid triples
for i in range(N):
    x = positions[i]
    # Check for triples
    if x + L / 3 in count_map: 
        ans += count_map[x + L / 3]
    if x + 2 * L / 3 in count_map: 
        ans += count_map[x + 2 * L / 3]
    
    # Add this position to the map
    if x in count_map: 
        count_map[x] += 1
    else: 
        count_map[x] = 1

print(ans)