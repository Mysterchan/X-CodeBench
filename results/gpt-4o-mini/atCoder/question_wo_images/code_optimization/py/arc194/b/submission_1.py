N = int(input())
P = list(map(int, input().split()))

# Create an array to hold the final positions of each element
position = [0] * N
for i in range(N):
    position[P[i] - 1] = i

# Calculate the total cost to sort the permutation
total_cost = 0
for i in range(N):
    while position[i] > i:
        total_cost += position[i]
        # Swap the current with the previous
        pos = position[i]
        position[P[pos - 1] - 1], position[P[pos] - 1] = pos, position[P[pos - 1] - 1]
        P[pos - 1], P[pos] = P[pos], P[pos - 1]
        # Update the new position of the element being moved
        position[i] -= 1

print(total_cost)