# Mapping for each direction and its opposite
direction_opposite = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
    'NE': 'SW',
    'SW': 'NE',
    'NW': 'SE',
    'SE': 'NW'
}

# Read the input direction
D = input().strip()

# Output the opposite direction
print(direction_opposite[D])