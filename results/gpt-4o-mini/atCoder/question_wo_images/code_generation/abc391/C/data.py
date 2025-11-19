import sys
input = sys.stdin.read

def pigeon_nests():
    data = input().splitlines()
    N, Q = map(int, data[0].split())
    
    # Initialize current positions of pigeons and the count of pigeons in nests
    pigeon_positions = list(range(1, N + 1))  # pigeon i is in nest i initially
    nest_counts = [0] * (N + 1)  # nest_counts[i] will hold the number of pigeons in nest i
    for i in range(1, N + 1):
        nest_counts[i] = 1  # initially each nest has one pigeon
    count_of_nests_with_multiple_pigeons = 0  # to track how many nests have more than one pigeon

    result = []

    for i in range(1, Q + 1):
        query = list(map(int, data[i].split()))
        if query[0] == 1:  # Move pigeon P to nest H
            P, H = query[1], query[2]
            current_nest = pigeon_positions[P - 1]  # Get current nest of pigeon P
            
            # Update the count for the current nest
            nest_counts[current_nest] -= 1
            if nest_counts[current_nest] == 1:  # Exactly 1 pigeon left now
                count_of_nests_with_multiple_pigeons -= 1
            elif nest_counts[current_nest] == 0:  # No pigeons left now
                nest_counts[current_nest] = 0
            
            # Move pigeon P to nest H
            pigeon_positions[P - 1] = H
            nest_counts[H] += 1
            
            if nest_counts[H] == 2:  # Exactly 2 pigeons now in nest H
                count_of_nests_with_multiple_pigeons += 1

        elif query[0] == 2:  # Output nests with more than one pigeon
            result.append(str(count_of_nests_with_multiple_pigeons))
    
    # Output all results for query type 2
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    pigeon_nests()