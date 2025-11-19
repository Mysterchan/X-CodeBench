import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    N, Q = map(int, data[0].split())
    
    # Initialize nests
    nests = list(range(N + 1))  # nests[i] = i means pigeon i is in nest i

    output = []
    
    for i in range(1, Q + 1):
        operation = list(map(int, data[i].split()))
        
        if operation[0] == 1:  # Type 1: Move pigeon a to nest b
            a, b = operation[1], operation[2]
            nests[a] = b
        
        elif operation[0] == 2:  # Type 2: Swap nests a and b
            a, b = operation[1], operation[2]
            # Swap the nests of all pigeons in nest a and b
            for j in range(1, N + 1):
                if nests[j] == a:
                    nests[j] = b
                elif nests[j] == b:
                    nests[j] = a
        
        elif operation[0] == 3:  # Type 3: Report the nest of pigeon a
            a = operation[1]
            output.append(nests[a])
    
    # Print all results for Type 3 operations
    sys.stdout.write('\n'.join(map(str, output)) + '\n')

if __name__ == "__main__":
    main()