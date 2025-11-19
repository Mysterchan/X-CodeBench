def solve():
    N = int(input())
    A = input().strip()
    
    # Memoization for minimum cost to achieve each value at each position
    memo = {}
    
    def min_cost(level, start, target):
        """
        Returns minimum cost to make position 'start' at 'level' equal to 'target'
        level 0 is the original string
        level N is the final single bit
        """
        if (level, start, target) in memo:
            return memo[(level, start, target)]
        
        if level == 0:
            # Base case: at leaf level
            current = int(A[start])
            cost = 0 if current == target else 1
            memo[(level, start, target)] = cost
            return cost
        
        # At this level, we need to check 3 children
        length = 3 ** (level - 1)
        child_positions = [start, start + length, start + 2 * length]
        
        # To make this position equal to target, we need at least 2 out of 3 children to be target
        costs = []
        for child_pos in child_positions:
            cost_0 = min_cost(level - 1, child_pos, 0)
            cost_1 = min_cost(level - 1, child_pos, 1)
            costs.append((cost_0, cost_1))
        
        if target == 0:
            # Need at least 2 children to be 0
            # Try all combinations where at least 2 are 0
            options = []
            # All three are 0
            options.append(costs[0][0] + costs[1][0] + costs[2][0])
            # Exactly two are 0
            options.append(costs[0][0] + costs[1][0] + costs[2][1])
            options.append(costs[0][0] + costs[1][1] + costs[2][0])
            options.append(costs[0][1] + costs[1][0] + costs[2][0])
            result = min(options)
        else:
            # Need at least 2 children to be 1
            options = []
            # All three are 1
            options.append(costs[0][1] + costs[1][1] + costs[2][1])
            # Exactly two are 1
            options.append(costs[0][1] + costs[1][1] + costs[2][0])
            options.append(costs[0][1] + costs[1][0] + costs[2][1])
            options.append(costs[0][0] + costs[1][1] + costs[2][1])
            result = min(options)
        
        memo[(level, start, target)] = result
        return result
    
    # First, find what the current final value is
    def get_final_value():
        current = [int(c) for c in A]
        for _ in range(N):
            next_level = []
            for i in range(0, len(current), 3):
                group = current[i:i+3]
                majority = 1 if sum(group) >= 2 else 0
                next_level.append(majority)
            current = next_level
        return current[0]
    
    final_value = get_final_value()
    target_value = 1 - final_value
    
    # Find minimum cost to change to target_value
    answer = min_cost(N, 0, target_value)
    print(answer)

solve()