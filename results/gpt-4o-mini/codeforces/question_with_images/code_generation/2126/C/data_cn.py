t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    
    # Since k is 1-indexed in the input, convert it to 0-indexed
    k -= 1
    max_height = max(heights)
    
    # Starting conditions
    current_height = heights[k]
    time = 1  # initial water level
    
    # Conditions to escape being drowned
    can_escape = False
    
    # Check if we can go to a tower with max height
    if current_height >= max_height:
        can_escape = True
    else:
        # Search to the left and right of the current position
        for step in range(max_height - current_height + 1):
            left = k - step
            right = k + step
            
            if left >= 0 and heights[left] >= max_height:
                can_escape = True
                break
            if right < n and heights[right] >= max_height:
                can_escape = True
                break
    
    print("YES" if can_escape else "NO")