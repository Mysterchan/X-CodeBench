def process_guests(num_cases, cases):
    results = []
    
    for case in cases:
        n, t = case
        table_counts = {}
        for i in range(n):
            t_i = t[i]
            if t_i == 0:
                # Guest wants an empty table
                # Iterate through the tables until we find an empty cell
                while True:
                    # Check from the smallest x and y cell
                    x = (len(table_counts) // 4)
                    y = len(table_counts) % 4
                    table_x = 3 * x + 1 + y // 2
                    table_y = 3 * (y % 2) + 1 + (y % 2)
                    if (table_x, table_y) not in table_counts:
                        # Found an empty table cell
                        table_counts[(table_x, table_y)] = True
                        results.append(f"{table_x} {table_y}")
                        break
            
            elif t_i == 1:
                # Guest wants the nearest available table cell
                min_distance = float('inf')
                selected_cell = None
                
                for x in range((n // 3) + 2):
                    for y in range((n // 3) + 2):
                        table_x = 3 * x + 1
                        table_y = 3 * y + 1
                        if (table_x, table_y) not in table_counts:
                            distance = abs(table_x) + abs(table_y)
                            if distance < min_distance:
                                min_distance = distance
                                selected_cell = (table_x, table_y)
                            elif distance == min_distance:
                                if (table_x, table_y) < selected_cell:
                                    selected_cell = (table_x, table_y)
                
                # Mark the selected cell as occupied
                table_counts[selected_cell] = True
                results.append(f"{selected_cell[0]} {selected_cell[1]}")
    
    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    q = int(data[0])
    cases = []
    idx = 1
    for _ in range(q):
        n = int(data[idx])
        t_list = list(map(int, data[idx + 1].split()))
        cases.append((n, t_list))
        idx += 2
    
    result = process_guests(q, cases)
    print("\n".join(result))