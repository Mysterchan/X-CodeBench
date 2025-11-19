D = input().strip()

opposites = {
    "N": "S",
    "E": "W",
    "W": "E",
    "S": "N",
    "NE": "SW",
    "NW": "SE",
    "SE": "NW",
    "SW": "NE"
}

print(opposites[D])