def can_form_sequence(X, Y, Z):
    # Calculate the total length of the sequence
    total = X + Y + Z
    
    # Check the conditions for forming a valid sequence
    if max(X, Y, Z) > (total + 1) // 2:
        return "No"
    return "Yes"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        X, Y, Z = map(int, data[i].split())
        results.append(can_form_sequence(X, Y, Z))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()