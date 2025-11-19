def main():
    D = input().strip()
    opposites = {
        'N': 'S', 'S': 'N',
        'E': 'W', 'W': 'E',
        'NE': 'SW', 'SW': 'NE',
        'NW': 'SE', 'SE': 'NW'
    }
    print(opposites[D])

if __name__ == "__main__":
    main()