def move_sliders(n, m, q, a, operations):
    MOD = 10**9 + 7
    result = [0] * n
    
    # Total sums for each position initially
    total_sum = sum(a)
    
    for k in range(q):
        i, x = operations[k]
        index = i - 1  # Convert to zero-indexed
        
        # Backup original positions
        orig_a = a[:]
        
        # Apply the operation while resolving collisions
        a[index] = x
        
        # Push sliders to the right if needed
        for j in range(index + 1, n):
            if a[j] <= x:  # Collision
                x = a[j]  # Move it to the colliding position
                a[j] += 1  # Move the next slider one position to the right
        
        # Push sliders to the left if the moved one affects them
        for j in range(index - 1, -1, -1):
            if a[j] >= x:  # Collision
                a[j] = x - 1  # Move the previous slider to the colliding position
                x = a[j]  # Update x for the next positions
        
        # Calculate the contribution of this operation to the result
        for j in range(n):
            result[j] = (result[j] + a[j]) % MOD
        
        # Restore original positions for the next operation
        a = orig_a
    
    # Each position was counted q! times, divide by fact(q) ( modular inverse )
    from math import factorial
    inv_fact_q = pow(factorial(q), MOD-2, MOD)
    result = [(res * inv_fact_q) % MOD for res in result]
    
    return result


def process_inputs():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n, m, q = map(int, data[index].split())
        a = list(map(int, data[index + 1].split()))
        operations = [tuple(map(int, data[index + i + 2].split())) for i in range(q)]
        index += (q + 2)
        
        result = move_sliders(n, m, q, a, operations)
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))


if __name__ == "__main__":
    process_inputs()