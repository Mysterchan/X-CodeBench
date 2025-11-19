def solve():
    N, W = map(int, input().split())
    items = []
    for _ in range(N):
        x, y = map(int, input().split())
        items.append((x, y))
    
    # Separate items into heavy and light
    threshold = 40
    heavy = []  # X_i >= threshold
    light = []  # X_i < threshold
    
    for x, y in items:
        if x >= threshold:
            heavy.append((x, y))
        else:
            light.append((x, y))
    
    # For light items, keep only best value for each weight
    weight_to_value = {}
    for x, y in light:
        weight = 1 << x
        if weight not in weight_to_value:
            weight_to_value[weight] = y
        else:
            weight_to_value[weight] = max(weight_to_value[weight], y)
    
    light_items = [(w, v) for w, v in weight_to_value.items()]
    
    # DP for light items with limited weight
    max_light_weight = min(W, (1 << threshold) - 1)
    dp = [0] * (max_light_weight + 1)
    
    for weight, value in light_items:
        if weight > max_light_weight:
            continue
        for w in range(max_light_weight, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    
    # Try all subsets of heavy items
    max_value = 0
    for mask in range(1 << len(heavy)):
        heavy_weight = 0
        heavy_value = 0
        
        for i in range(len(heavy)):
            if mask & (1 << i):
                x, y = heavy[i]
                heavy_weight += (1 << x)
                heavy_value += y
                if heavy_weight > W:
                    break
        
        if heavy_weight > W:
            continue
        
        # Find best light items that fit in remaining weight
        remaining = W - heavy_weight
        if remaining > max_light_weight:
            remaining = max_light_weight
        
        total_value = heavy_value + dp[remaining]
        max_value = max(max_value, total_value)
    
    return max_value

T = int(input())
for _ in range(T):
    print(solve())