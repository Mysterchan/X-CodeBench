def find_tables(q, cases):
    results = []
    for case in cases:
        n, t = case
        occupied = set()
        table_positions = []
        
        # All possible table positions with coordinates (3x+1, 3y+1), (3x+1, 3y+2), 
        # (3x+2, 3y+1), (3x+2, 3y+2) for x, y >= 0
        for x in range(100):  # limited to reasonable range for casual observation
            for y in range(100):
                table_positions.append((3 * x + 1, 3 * y + 1))
                table_positions.append((3 * x + 1, 3 * y + 2))
                table_positions.append((3 * x + 2, 3 * y + 1))
                table_positions.append((3 * x + 2, 3 * y + 2))
        
        for guest in range(n):
            if t[guest] == 1:  # Strategy 1: Move to closest available table
                min_distance = float('inf')
                chosen_table = None
                for table in table_positions:
                    if table not in occupied:
                        distance = abs(table[0] - 0) + abs(table[1] - 0)
                        if distance < min_distance:
                            min_distance = distance
                            chosen_table = table
                        elif distance == min_distance:
                            if chosen_table is None or (table < chosen_table):
                                chosen_table = table
                results.append(chosen_table)
                occupied.add(chosen_table)
            else:  # Strategy 0: Move to nearest empty table
                min_distance = float('inf')
                chosen_table = None
                for table in table_positions:
                    if table not in occupied:
                        distance = abs(table[0] - 0) + abs(table[1] - 0)
                        if distance < min_distance:
                            min_distance = distance
                            chosen_table = table
                        elif distance == min_distance:
                            if chosen_table is None or (table < chosen_table):
                                chosen_table = table
                results.append(chosen_table)
                occupied.add(chosen_table)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
cases = []
line_index = 1

for _ in range(q):
    n = int(data[line_index])
    t = list(map(int, data[line_index + 1].split()))
    cases.append((n, t))
    line_index += 2

# Find the results
result_positions = find_tables(q, cases)

# Output results
for pos in result_positions:
    print(pos[0], pos[1])