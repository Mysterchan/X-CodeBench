N = int(input())

for r in range(1, N + 1):
    row = []
    for c in range(1, N + 1):
        # Find the last operation that affects this cell
        last_i = min(r, c, N + 1 - r, N + 1 - c)
        
        # Determine color based on whether last_i is odd or even
        if last_i % 2 == 1:
            row.append('#')
        else:
            row.append('.')
    
    print(''.join(row))