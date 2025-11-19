def knapsack(test_cases):
    results = []
    for N, W, items in test_cases:
        # Collect pairs of weights and values
        weight_value_pairs = [(2**x, y) for x, y in items]
        
        # Sort items by weight first and then value (both in descending order)
        weight_value_pairs.sort(key=lambda item: (item[0], item[1]), reverse=True)
        
        total_value = 0
        total_weight = 0
        
        for weight, value in weight_value_pairs:
            if total_weight + weight <= W:
                total_weight += weight
                total_value += value
                
        results.append(total_value)
    
    return results


import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    index = 0
    T = int(data[index])
    index += 1
    test_cases = []
    
    for _ in range(T):
        N, W = map(int, data[index].split())
        index += 1
        items = []
        
        for _ in range(N):
            x, y = map(int, data[index].split())
            items.append((x, y))
            index += 1
        
        test_cases.append((N, W, items))
    
    results = knapsack(test_cases)
    
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()