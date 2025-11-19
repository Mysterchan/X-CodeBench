# Mapping of directions to their opposites
opposite_directions = {
    "N": "S",
    "E": "W",
    "W": "E",
    "S": "N",
    "NE": "SW",
    "NW": "SE",
    "SE": "NW",
    "SW": "NE"
}

# Read input direction
D = input().strip()

# Print the opposite direction
print(opposite_directions[D])