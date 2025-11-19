def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    # Use memoization with state as tuple of sorted partition sums
    memo = {}
    
    def dp(index, partitions):
        # partitions is a tuple of current sums in each group
        if index == N:
            # Compute XOR of all partition sums
            result = 0
            for s in partitions:
                result ^= s
            return {result}
        
        # Convert to tuple for hashing
        state = (index, partitions)
        if state in memo:
            return memo[state]
        
        results = set()
        
        # Try adding current bag to each existing partition
        for i in range(len(partitions)):
            new_partitions = list(partitions)
            new_partitions[i] += A[index]
            results.update(dp(index + 1, tuple(new_partitions)))
        
        # Try creating a new partition
        new_partitions = list(partitions) + [A[index]]
        results.update(dp(index + 1, tuple(new_partitions)))
        
        memo[state] = results
        return results
    
    result = dp(0, ())
    print(len(result))

solve()