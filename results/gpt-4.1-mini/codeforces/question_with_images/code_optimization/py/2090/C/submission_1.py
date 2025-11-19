def main():
    import sys
    input = sys.stdin.readline

    # Precompute candidates and tables once
    BOUND = 320
    table_status = [(i, j) for i in range(BOUND + 1) for j in range(BOUND - i + 1)]

    # Precompute all candidate seats with their distances and coordinates
    # Distance = 3*(i+j) + offset for each seat in the table
    # Seats: (3i+1,3j+1) dist +2, (3i+1,3j+2) dist +3, (3i+2,3j+1) dist +3, (3i+2,3j+2) dist +6
    cand_list = []
    for i, j in table_status:
        base = 3 * (i + j)
        cand_list.append((base + 2, 3 * i + 1, 3 * j + 1, i, j, 0))
        cand_list.append((base + 3, 3 * i + 1, 3 * j + 2, i, j, 1))
        cand_list.append((base + 3, 3 * i + 2, 3 * j + 1, i, j, 2))
        cand_list.append((base + 6, 3 * i + 2, 3 * j + 2, i, j, 3))
    cand_list.sort(key=lambda x: (x[0], x[1], x[2]))

    # Precompute heap of tables by their minimal seat (distance, x, y)
    import heapq
    avail_tables = []
    for i, j in table_status:
        dist = 3 * (i + j) + 2
        x, y = 3 * i + 1, 3 * j + 1
        heapq.heappush(avail_tables, (dist, x, y, i, j))

    q = int(input())
    out = []
    for _ in range(q):
        n = int(input())
        t = list(map(int, input().split()))

        # For each test case, reset table occupancy and heap
        cur_table_status = [0] * len(table_status)
        # Map (i,j) to index for O(1) access
        idx_map = {}
        for idx, (i, j) in enumerate(table_status):
            idx_map[(i, j)] = idx

        # Copy heap for current test case
        cur_avail = avail_tables[:]
        heapq.heapify(cur_avail)

        cand_ptr = 0
        for gt in t:
            if gt == 1:
                # Find next free seat in cand_list
                while True:
                    d, cx, cy, ti, tj, seat_type = cand_list[cand_ptr]
                    idx = idx_map[(ti, tj)]
                    if (cur_table_status[idx] & (1 << seat_type)) == 0:
                        break
                    cand_ptr += 1
                # Occupy seat
                cur_table_status[idx] |= (1 << seat_type)
                out.append(f"{cx} {cy}")
                cand_ptr += 1
            else:
                # Find next completely free table
                while cur_avail:
                    dist, ax, ay, ti, tj = cur_avail[0]
                    idx = idx_map[(ti, tj)]
                    if cur_table_status[idx] == 0:
                        break
                    heapq.heappop(cur_avail)
                if cur_avail:
                    dist, ax, ay, ti, tj = heapq.heappop(cur_avail)
                    idx = idx_map[(ti, tj)]
                    # Occupy seat (0) in this table
                    cur_table_status[idx] |= 1
                    out.append(f"{ax} {ay}")
                else:
                    # No free table, fallback to any free seat (like gt=1)
                    while True:
                        d, cx, cy, ti, tj, seat_type = cand_list[cand_ptr]
                        idx = idx_map[(ti, tj)]
                        if (cur_table_status[idx] & (1 << seat_type)) == 0:
                            break
                        cand_ptr += 1
                    cur_table_status[idx] |= (1 << seat_type)
                    out.append(f"{cx} {cy}")
                    cand_ptr += 1

    print("\n".join(out))


if __name__ == "__main__":
    main()