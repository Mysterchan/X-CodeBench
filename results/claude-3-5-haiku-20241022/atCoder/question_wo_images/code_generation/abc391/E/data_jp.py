def solve():
    N = int(input())
    A = input().strip()
    
    def majority(a, b, c):
        return 1 if a + b + c >= 2 else 0
    
    def min_changes_to_flip(arr, level):
        if level == 0:
            return 1 if arr[0] == 1 else 1
        
        n = 3 ** level
        chunk_size = n // 3
        
        results = []
        for i in range(3):
            start = i * chunk_size
            end = start + chunk_size
            chunk = arr[start:end]
            results.append(min_changes_to_flip(chunk, level - 1))
        
        current = majority(
            1 if results[0] <= chunk_size else 0,
            1 if results[1] <= chunk_size else 0,
            1 if results[2] <= chunk_size else 0
        )
        
        results.sort()
        
        if current == 1:
            return results[0] + results[1]
        else:
            return results[0]
    
    def compute_final(arr, level):
        if level == 0:
            return arr[0]
        
        n = 3 ** level
        chunk_size = n // 3
        
        results = []
        for i in range(3):
            start = i * chunk_size
            end = start + chunk_size
            chunk = arr[start:end]
            results.append(compute_final(chunk, level - 1))
        
        return majority(results[0], results[1], results[2])
    
    def min_changes(arr, level, target):
        if level == 0:
            return 0 if arr[0] == target else 1
        
        n = 3 ** level
        chunk_size = n // 3
        
        costs = []
        values = []
        for i in range(3):
            start = i * chunk_size
            end = start + chunk_size
            chunk = arr[start:end]
            val = compute_final(chunk, level - 1)
            values.append(val)
            cost0 = min_changes(chunk, level - 1, 0)
            cost1 = min_changes(chunk, level - 1, 1)
            costs.append((cost0, cost1))
        
        current = majority(values[0], values[1], values[2])
        
        if current == target:
            options = []
            for i in range(3):
                flip_cost = costs[i][1 - values[i]]
                options.append(flip_cost)
            
            options.sort()
            if target == 1:
                return options[0] + options[1]
            else:
                return options[0]
        else:
            total = 0
            for i in range(3):
                total += costs[i][target]
            return total
    
    A_list = [int(c) for c in A]
    final_value = compute_final(A_list, N)
    target = 1 - final_value
    answer = min_changes(A_list, N, target)
    
    print(answer)

solve()