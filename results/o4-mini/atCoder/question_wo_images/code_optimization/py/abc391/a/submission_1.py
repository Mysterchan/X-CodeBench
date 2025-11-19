import sys
def main():
    d = sys.stdin.readline().strip()
    opp = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E',
        'NE': 'SW',
        'SW': 'NE',
        'NW': 'SE',
        'SE': 'NW'
    }
    print(opp[d])

if __name__ == "__main__":
    main()