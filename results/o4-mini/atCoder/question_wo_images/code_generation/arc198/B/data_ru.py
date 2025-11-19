def can_form_sequence(X, Y, Z):
    # Check the conditions for forming a valid sequence
    if X > Y + Z + 1 or Y > X + Z + 1 or Z > X + Y + 1:
        return "No"
    return "Yes"

import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        X, Y, Z = map(int, data[i].split())
        results.append(can_form_sequence(X, Y, Z))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()