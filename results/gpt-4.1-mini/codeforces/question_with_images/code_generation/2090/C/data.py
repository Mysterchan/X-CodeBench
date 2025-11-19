import sys
input = sys.stdin.readline

# Each table has 4 cells:
# (3x+1, 3y+1), (3x+1, 3y+2), (3x+2, 3y+1), (3x+2, 3y+2)
# Distance from (0,0) to any of these cells is (3x+1)+(3y+1) = 3x+3y+2 or (3x+1)+(3y+2) = 3x+3y+3 etc.
# The minimal distance to a table is always 3*(x+y)+2 (for cell (3x+1,3y+1)) or +3 for others.
# The guests pick the nearest free cell according to distance, then by x, then by y.

# For t_i=0 guests: must pick a cell from a completely unoccupied table.
# For t_i=1 guests: pick any free table cell.

# We will assign cells in order of increasing distance.
# The order of tables by distance is by increasing (x+y), then by x.
# For each table, the 4 cells are:
# (3x+1, 3y+1), (3x+1, 3y+2), (3x+2, 3y+1), (3x+2, 3y+2)
# We assign cells in this order to maintain minimal x,y priority.

# Approach:
# - Maintain two queues:
#   1) tables with no occupied cells (for t=0 guests)
#   2) tables with some occupied cells but not full (for t=1 guests)
# - When a t=0 guest arrives, assign the first free cell of the first table in the no-occupied queue,
#   then move that table to the partially occupied queue.
# - When a t=1 guest arrives, assign the first free cell of the first table in the partially occupied queue.
#   If the table becomes full, remove it from the partially occupied queue.
# - If partially occupied queue is empty, assign from no-occupied queue (since t=1 guests can sit anywhere).
# - If no-occupied queue is empty, generate new tables in order of increasing (x+y), then x.

# We generate tables on demand, in order of increasing (x+y), then x.
# We keep track of the next table to generate.

from collections import deque

def solve():
    q = int(input())
    # Preprocessing is not needed, we generate tables on demand.

    # For each test case:
    for _ in range(q):
        n = int(input())
        t = list(map(int, input().split()))

        # Queues:
        # no_occ_tables: tables with 0 occupied cells
        # Each element: (x, y, occupied_cells_count, next_cell_index)
        # partially_occ_tables: tables with 1 to 3 occupied cells
        # Each element: (x, y, occupied_cells_count, next_cell_index)
        no_occ_tables = deque()
        partially_occ_tables = deque()

        # We generate tables in order of increasing (x+y), then x.
        # We'll keep a pointer to the next table to generate.
        # The maximum number of guests per test is 50,000, so generating tables on demand is feasible.

        # We'll generate tables with increasing sum = x+y starting from 0 upwards.
        # For each sum, x goes from 0 to sum, y = sum - x.

        # We'll keep track of the current sum and x for next table to generate.
        current_sum = 0
        current_x = 0

        # Function to generate next table and add to no_occ_tables
        def generate_next_table():
            nonlocal current_sum, current_x
            x = current_x
            y = current_sum - x
            no_occ_tables.append([x, y, 0, 0])  # occupied_cells_count=0, next_cell_index=0
            current_x += 1
            if current_x > current_sum:
                current_sum += 1
                current_x = 0

        # Pre-generate some tables to start with (at least one)
        generate_next_table()

        # The 4 cells in order for each table:
        # (3x+1, 3y+1), (3x+1, 3y+2), (3x+2, 3y+1), (3x+2, 3y+2)
        cells_offsets = [(1,1), (1,2), (2,1), (2,2)]

        output = []

        for ti in t:
            if ti == 0:
                # t=0 guest: must pick from a completely unoccupied table
                # If no such table, generate new tables until we have one
                while not no_occ_tables:
                    generate_next_table()
                # Assign the next free cell of the first no_occ_table
                table = no_occ_tables[0]
                x, y, occ_count, next_cell = table
                # next_cell must be 0 because table is unoccupied
                cx, cy = cells_offsets[next_cell]
                cell_x = 3*x + cx
                cell_y = 3*y + cy
                output.append(f"{cell_x} {cell_y}")
                # Update table info
                table[2] = 1  # now occupied count = 1
                table[3] = 1  # next cell index = 1
                # Move this table from no_occ_tables to partially_occ_tables
                no_occ_tables.popleft()
                partially_occ_tables.append(table)
            else:
                # t=1 guest: pick from nearest free table cell (any table)
                # Try partially occupied tables first
                while not partially_occ_tables and not no_occ_tables:
                    generate_next_table()
                if partially_occ_tables:
                    table = partially_occ_tables[0]
                else:
                    # no partially occupied tables, pick from no_occ_tables
                    # If empty, generate new table
                    while not no_occ_tables:
                        generate_next_table()
                    table = no_occ_tables[0]

                x, y, occ_count, next_cell = table
                cx, cy = cells_offsets[next_cell]
                cell_x = 3*x + cx
                cell_y = 3*y + cy
                output.append(f"{cell_x} {cell_y}")
                # Update table info
                table[2] += 1
                table[3] += 1
                if table[2] == 4:
                    # Table full, remove from partially_occ_tables if present
                    if partially_occ_tables and partially_occ_tables[0] == table:
                        partially_occ_tables.popleft()
                    else:
                        # If it was in no_occ_tables (should not happen for t=1), remove it
                        if no_occ_tables and no_occ_tables[0] == table:
                            no_occ_tables.popleft()
                else:
                    # If table was in no_occ_tables, move it to partially_occ_tables
                    if no_occ_tables and no_occ_tables[0] == table:
                        no_occ_tables.popleft()
                        partially_occ_tables.append(table)

            # Ensure we have enough tables generated for future guests
            # If no_occ_tables is empty, generate next table to keep supply
            if not no_occ_tables:
                generate_next_table()

        print('\n'.join(output))


if __name__ == "__main__":
    solve()