def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        people = []
        
        for i in range(N):
            L, R = map(int, data[index].split())
            people.append((L, R, i + 1))  # Store (L, R, original_index)
            index += 1
        
        # Sort people by (L, R) to minimize dissatisfaction
        people.sort()
        
        # Assign seats in the order of sorted people
        seats = [0] * N
        for seat_number in range(N):
            _, _, original_index = people[seat_number]
            seats[original_index - 1] = seat_number + 1  # Assign seat number (1-indexed)
        
        results.append(" ".join(map(str, seats)))
    
    print("\n".join(results))

solve()