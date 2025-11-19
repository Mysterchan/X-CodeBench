def opposite_direction(D):
    directions = {
        'N': 'S',
        'E': 'W',
        'W': 'E',
        'S': 'N',
        'NE': 'SW',
        'NW': 'SE',
        'SE': 'NW',
        'SW': 'NE'
    }
    return directions[D]

D = input().strip()
print(opposite_direction(D))