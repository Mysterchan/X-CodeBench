def find_path(N, K):
    path = []
    visits = [[0] * N for _ in range(N)]
    
    x, y = 0, 0  # Starting position (0-indexed)
    
    for _ in range(2 * N - 2):
        # If we can move down
        can_move_down = (x + 1 < N)
        # If we can move right
        can_move_right = (y + 1 < N)

        # Choosing the move
        if can_move_down and can_move_right:
            if visits[x + 1][y] < visits[x][y + 1]:
                path.append('D')
                x += 1
            elif visits[x + 1][y] > visits[x][y + 1]:
                path.append('R')
                y += 1
            else:
                # Counts are equal, prefer down
                path.append('D')
                x += 1
        elif can_move_down:
            path.append('D')
            x += 1
        elif can_move_right:
            path.append('R')
            y += 1

        visits[x][y] += 1  # Increment the visit count for the new cell
        
        # Simulate K visits
        if _ < K - 1:  # Update visit counts for next exercise
            visits[x][y] += 1

    return ''.join(path)

# Read input
N, K = map(int, input().split())
print(find_path(N, K))