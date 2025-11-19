def can_partition(n, ranges):
    total_cells = 0
    total_ranges = []
    
    for l, r in ranges:
        total_cells += (r - l + 1)
        total_ranges.append((l, r))
    
    # We need to check if total_cells can be split into two equal parts
    if total_cells % 2 != 0:
        return False

    half_cells = total_cells // 2
    occupied = set()
    # Build occupied cells
    for i in range(n):
        for j in range(total_ranges[i][0], total_ranges[i][1] + 1):
            occupied.add((i, j))

    # Try to partition the polyomino into two congruent parts
    for i in range(n):
        l1, r1 = total_ranges[i]
        segment_length = r1 - l1 + 1
        
        # Check if segment_length is even
        if segment_length % 2 != 0:
            return False
        
        # Determine the mid point
        mid = l1 + segment_length // 2
        
        # Create two parts and validate
        part1 = set()
        part2 = set()
        
        for j in range(total_ranges[i][0], total_ranges[i][1] + 1):
            if j < mid:
                part1.add((i, j))
            else:
                part2.add((i, j))

        # Now we should validate for connectivity of part1 and part2
        def is_connected(part):
            if not part:
                return True
            start = next(iter(part))
            visited = {start}
            queue = [start]
            while queue:
                x, y = queue.pop(0)
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (nx, ny) in part and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return len(visited) == len(part)

        if is_connected(part1) and is_connected(part2):
            return True
    
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    ranges = [tuple(map(int, input().split())) for _ in range(n)]
    if can_partition(n, ranges):
        print("YES")
    else:
        print("NO")