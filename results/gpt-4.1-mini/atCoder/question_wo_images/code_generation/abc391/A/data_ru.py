D = input().strip()

opposites = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
    'NE': 'SW',
    'NW': 'SE',
    'SE': 'NW',
    'SW': 'NE'
}

print(opposites[D])