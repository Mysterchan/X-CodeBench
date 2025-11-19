def main():
    import sys
    D = sys.stdin.readline().strip()
    opp = {
        "N": "S",
        "S": "N",
        "E": "W",
        "W": "E",
        "NE": "SW",
        "SW": "NE",
        "NW": "SE",
        "SE": "NW"
    }
    print(opp[D])

if __name__ == "__main__":
    main()