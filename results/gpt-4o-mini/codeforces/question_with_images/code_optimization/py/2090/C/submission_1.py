def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    index = 1
    
    max_guests = 0
    guests_per_test = []
    
    for _ in range(q):
        n = int(data[index])
        index += 1
        guests = list(map(int, data[index:index + n]))
        guests_per_test.append((n, guests))
        max_guests = max(max_guests, n)
        index += n
    
    table_positions = []
    
    # Precompute table positions
    for i in range(320):  # This 320 is enough considering the bounds
        for j in range(320 - i):
            x1, y1 = 3 * i + 1, 3 * j + 1
            x2, y2 = 3 * i + 1, 3 * j + 2
            x3, y3 = 3 * i + 2, 3 * j + 1
            x4, y4 = 3 * i + 2, 3 * j + 2
            table_positions.append((x1, y1, (i, j, 0)))
            table_positions.append((x2, y2, (i, j, 1)))
            table_positions.append((x3, y3, (i, j, 2)))
            table_positions.append((x4, y4, (i, j, 3)))
    
    # Sort table positions by coordinates
    table_positions.sort()

    output = []
    
    for n, guests in guests_per_test:
        cur_table_status = {}
        available_tables = set()
        
        for x, y, (i, j, seat_type) in table_positions:
            available_tables.add((x, y, i, j, seat_type))
        
        for guest_type in guests:
            if guest_type == 1:  # Nearest free table
                for x, y, (i, j, seat_type) in table_positions:
                    if (i, j) not in cur_table_status or cur_table_status[(i, j)] & (1 << seat_type) == 0:
                        if (i, j) not in cur_table_status:
                            cur_table_status[(i, j)] = 0
                        cur_table_status[(i, j)] |= (1 << seat_type)
                        output.append(f"{x} {y}")
                        break
            else:  # Nearest completely unoccupied table
                for x, y, (i, j, seat_type) in table_positions:
                    if (i, j) not in cur_table_status or cur_table_status[(i, j)] == 0:
                        if (i, j) not in cur_table_status:
                            cur_table_status[(i, j)] = 0
                        cur_table_status[(i, j)] |= (1 << seat_type)
                        output.append(f"{x} {y}")
                        break
    
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    main()