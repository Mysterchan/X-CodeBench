def count_possible_xor_values(n, stones):
    possible_values = set()
    
    # Start with the xor being 0, as taking all stones to one bag gives that result.
    possible_values.add(0)
    
    # Calculate all possible xor values using two physical bags.
    for i in range(n):
        current_bag = stones[i]
        new_possible_values = set()
        for existing_xor in possible_values:
            # We can either keep the existing XOR value
            new_possible_values.add(existing_xor)
            # Or add the current bag's stones to it
            new_possible_values.add(existing_xor ^ current_bag)
        
        # Update possible values
        possible_values = new_possible_values
    
    return len(possible_values)

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))

# Get the result and print
result = count_possible_xor_values(N, A)
print(result)