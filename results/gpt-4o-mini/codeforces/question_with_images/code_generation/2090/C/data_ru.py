def find_table(q, guests_list):
    results = []
    occupied_tables = set()
    
    for guests in guests_list:
        n, types = guests
        for i in range(n):
            t_i = types[i]
            # Determine the available table position
            found = False
            if t_i == 1:  # Looking for the nearest table
                x, y = 0, 0
                while not found:
                    for dx in range(3):
                        for dy in range(3):
                            table_x = 3 * x + dx
                            table_y = 3 * y + dy
                            if (table_x, table_y) not in occupied_tables:
                                found = True
                                results.append((table_x, table_y))
                                occupied_tables.add((table_x, table_y))
                                break
                        if found:
                            break
                    if not found:
                        y += 1  # Move to the next row of tables
            else:  # Looking for completely unoccupied table
                for local_x in range(7):  # Check next 7 rows/columns
                    for local_y in range(7):
                        table_x = local_x * 3 + 1
                        table_y = local_y * 3 + 1
                        if (table_x, table_y) not in occupied_tables:
                            found = True
                            results.append((table_x, table_y))
                            occupied_tables.add((table_x, table_y))
                            break
                    if found:
                        break

    return results


q = int(input())
guests_list = []
for _ in range(q):
    n = int(input())
    types = list(map(int, input().split()))
    guests_list.append((n, types))

results = find_table(q, guests_list)
for x, y in results:
    print(x, y)