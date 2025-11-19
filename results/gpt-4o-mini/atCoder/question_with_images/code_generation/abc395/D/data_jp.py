import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    N, Q = map(int, data[0].split())
    
    # Initialize the nests
    nests = list(range(1, N + 1))
    
    output = []
    
    for i in range(1, Q + 1):
        operation = list(map(int, data[i].split()))
        
        if operation[0] == 1:
            # Move pigeon a to nest b
            a, b = operation[1] - 1, operation[2] - 1
            nests[a] = b + 1
            
        elif operation[0] == 2:
            # Swap nests a and b
            a, b = operation[1] - 1, operation[2] - 1
            nests[a], nests[b] = nests[b], nests[a]
        
        elif operation[0] == 3:
            # Report the nest of pigeon a
            a = operation[1] - 1
            output.append(nests[a])
    
    # Print all results for type 3 operations
    print('\n'.join(map(str, output)))

if __name__ == "__main__":
    main()