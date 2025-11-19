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
    print(directions[D])

D = input().strip()
opposite_direction(D)