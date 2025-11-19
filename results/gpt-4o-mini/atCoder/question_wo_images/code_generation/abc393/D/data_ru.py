N = int(input())
S = input().strip()

positions = [i for i, char in enumerate(S) if char == '1']
count = 0

# We want to move all '1's together starting from their first position
# and creating a compact group
for i, position in enumerate(positions):
    # The goal is for the ith '1' to be in the position of the first '1' plus i
    target_position = positions[0] + i
    count += position - target_position

print(count)