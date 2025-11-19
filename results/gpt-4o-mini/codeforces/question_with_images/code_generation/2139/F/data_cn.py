def simulate_moves(n, m, q, positions, moves):
    mod = 10**9 + 7
    position_sum = [0] * n
    factorial = 1

    for i in range(1, q + 1):
        factorial = (factorial * i) % mod

    # Store the final positions for each wood based on the moves
    for move in moves:
        original_positions = positions[:]
        
        i, x = move
        i -= 1  # Convert to 0-indexed
        
        # Perform the move with collision handling
        # Move wood `i` to position `x`
        current_pos = original_positions[i]
        original_positions[i] = x
        
        # Handle pushing
        if current_pos < x:  # Moving right
            for j in range(i + 1, n):
                if original_positions[j] <= x:
                    x += 1
                else:
                    break
            original_positions[i] = x
            
        else:  # Moving left
            for j in range(i - 1, -1, -1):
                if original_positions[j] >= x:
                    x -= 1
                else:
                    break
            original_positions[i] = x

        # Add the final positions to the sum
        for j in range(n):
            position_sum[j] = (position_sum[j] + original_positions[j]) % mod

    # Multiply by the factorial of q (the number of permutations)
    for j in range(n):
        position_sum[j] = (position_sum[j] * factorial) % mod
        
    return position_sum


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m, q = map(int, data[index:index + 3])
        index += 3
        positions = list(map(int, data[index:index + n]))
        index += n
        moves = [tuple(map(int, data[index + i:index + i + 2])) for i in range(0, q * 2, 2)]
        index += q * 2
        
        result = simulate_moves(n, m, q, positions, moves)
        results.append(" ".join(map(str, result)))
    
    print("\n".join(results))


if __name__ == "__main__":
    main()