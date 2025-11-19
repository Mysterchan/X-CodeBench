def find_tables(q, cases):
    results = []
    occupied = set()  # Track occupied tables

    for case in cases:
        n, types = case
        choice_map = []  # Store chosen tables for current case
        
        for i in range(n):
            t = types[i]
            if t == 1:
                # Find the nearest table
                found = False
                for dist in range(0, 100):  # A reasonable distance limit
                    if found:
                        break
                    for x in range(dist // 3 + 1):  # 3x + 1 < sqrt(3 dist)
                        for y in range(dist // 3 + 1):
                            if (x + y) * 3 > dist:
                                break
                            table_positions = [
                                (3 * x + 1, 3 * y + 1),
                                (3 * x + 1, 3 * y + 2),
                                (3 * x + 2, 3 * y + 1),
                                (3 * x + 2, 3 * y + 2),
                            ]
                            for pos in table_positions:
                                if pos not in occupied:
                                    occupied.add(pos)
                                    choice_map.append(pos)
                                    found = True
                                    break
            else:
                # Find a completely unoccupied table
                found = False
                for dist in range(0, 100):  # A reasonable distance limit
                    if found:
                        break
                    for x in range(dist // 3 + 1):  # 3x + 1 < sqrt(3 dist)
                        for y in range(dist // 3 + 1):
                            if (x + y) * 3 > dist:
                                break
                            table_positions = [
                                (3 * x + 1, 3 * y + 1),
                                (3 * x + 1, 3 * y + 2),
                                (3 * x + 2, 3 * y + 1),
                                (3 * x + 2, 3 * y + 2),
                            ]
                            for pos in table_positions:
                                if pos not in occupied:
                                    occupied.add(pos)
                                    choice_map.append(pos)
                                    found = True
                                    break
            
        results.append(choice_map)
    
    return results

# Read input
q = int(input())
cases = []
for _ in range(q):
    n = int(input())
    types = list(map(int, input().split()))
    cases.append((n, types))

# Get results and print
results = find_tables(q, cases)
for case_result in results:
    for pos in case_result:
        print(pos[0], pos[1])