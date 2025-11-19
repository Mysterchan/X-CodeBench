def game_winner(n, m, k, positions):
    from collections import defaultdict
    
    # Mark positions of coins
    grid = defaultdict(int)
    for x, y in positions:
        grid[(x, y)] += 1

    # Create a list to count valid rows for each column
    choices = [0] * (n + 1)

    # Iterate through each row from top to bottom
    for row in range(1, n + 1):
        # We need to check columns from m to 1
        for col in range(m, 0, -1):
            # For the first column, if there's a coin, we can use it
            if col == 1:
                choices[row] += grid[(row, col)]
            else:
                # Add valid coins to the current row's choices
                if grid[(row, col)] > 0:
                    # We can only use coins in column col and move left to col - 1
                    choices[row] += grid[(row, col)]
                else:
                    # If there are no coins in column col, we break since we can't move left
                    break

    # Calculate the xor sum of all available moves
    xor_sum = 0
    for row in range(1, n + 1):
        xor_sum ^= choices[row]

    # Determine the winner based on the xor sum
    return "Mimo" if xor_sum != 0 else "Yuyu"

import sys

input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
output = []

index = 1
for _ in range(t):
    n, m, k = map(int, data[index].split())
    positions = [tuple(map(int, data[index + i + 1].split())) for i in range(k)]
    index += k + 1
    output.append(game_winner(n, m, k, positions))

print("\n".join(output))