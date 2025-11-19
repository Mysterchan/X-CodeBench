def main():
    import sys
    
    # Read the input direction
    D = sys.stdin.readline().strip()
    
    # Mapping of each cardinal/intercardinal component to its opposite
    opposite = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
    }
    
    # Build the opposite direction by replacing each character
    result = ''.join(opposite[c] for c in D)
    
    # Output the result
    print(result)

if __name__ == "__main__":
    main()