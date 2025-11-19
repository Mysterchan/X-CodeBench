def can_partition(n, ranges):
    cells = set()
    for i in range(n):
        for j in range(ranges[i][0], ranges[i][1] + 1):
            cells.add((i, j))
    
    total_area = len(cells)
    half_area = total_area // 2
    
    for dx in range(-n, n + 1):
        for dy in range(-10, 11):
            if dx == 0 and dy == 0:
                continue
            
            valid = True
            part1 = set()
            part2 = set()
            
            for cell in cells:
                x, y = cell
                translated = (x + dx, y + dy)
                
                if translated in cells:
                    if cell not in part2:
                        part1.add(cell)
                        part2.add(translated)
            
            if len(part1) != half_area:
                continue
            
            if part1.union(part2) != cells:
                continue
            
            if part1.intersection(part2):
                continue
            
            def is_connected(part):
                if not part:
                    return False
                start = next(iter(part))
                visited = {start}
                queue = [start]
                
                while queue:
                    x, y = queue.pop(0)
                    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
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
    ranges = []
    for _ in range(n):
        l, r = map(int, input().split())
        ranges.append((l, r))
    
    if can_partition(n, ranges):
        print("YES")
    else:
        print("NO")
        