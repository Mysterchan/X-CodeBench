def solve():
    N = int(input())
    A = input().strip()
    
    def apply_operation(s):
        result = []
        for i in range(0, len(s), 3):
            group = s[i:i+3]
            count_ones = group.count('1')
            result.append('1' if count_ones >= 2 else '0')
        return ''.join(result)
    
    def get_final_value(s):
        current = s
        for _ in range(N):
            current = apply_operation(current)
        return current[0]
    
    original_final = get_final_value(A)
    target = '0' if original_final == '1' else '1'
    
    def min_changes(s, level, target_val):
        if level == 0:
            return 0 if s[0] == target_val else 1
        
        length = 3 ** level
        third = length // 3
        
        chunks = [s[i*third:(i+1)*third] for i in range(3)]
        
        costs = []
        for chunk in chunks:
            cost_0 = min_changes(chunk, level - 1, '0')
            cost_1 = min_changes(chunk, level - 1, '1')
            costs.append((cost_0, cost_1))
        
        min_cost = float('inf')
        
        for mask in range(8):
            values = []
            total_cost = 0
            for i in range(3):
                if mask & (1 << i):
                    values.append('1')
                    total_cost += costs[i][1]
                else:
                    values.append('0')
                    total_cost += costs[i][0]
            
            majority = '1' if values.count('1') >= 2 else '0'
            if majority == target_val:
                min_cost = min(min_cost, total_cost)
        
        return min_cost
    
    result = min_changes(A, N, target)
    print(result)

solve()