def determine_winner(n, m, tokens):
    # Create a column occupancy count
    column_count = [0] * (m + 1)
    
    # Count tokens in columns
    for _, col in tokens:
        column_count[col] += 1
    
    # Check if there's any valid move for Mimo
    if column_count[1] == 0:
        return "Yuyu"
    
    # Determine the winner based on the number of tokens in the first column
    for col in range(2, m + 1):
        if column_count[col] > 0:
            return "Mimo"

    # If only the first column has tokens
    return "Mimo" if (len(tokens) % 2 == 1) else "Yuyu"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    test_cases = int(data[0])
    index = 1
    results = []
    
    for _ in range(test_cases):
        n, m, k = map(int, data[index].split())
        index += 1
        tokens = [tuple(map(int, data[index + i].split())) for i in range(k)]
        index += k
        
        results.append(determine_winner(n, m, tokens))
    
    # Output all results at once to minimize print calls
    print("\n".join(results))

main()