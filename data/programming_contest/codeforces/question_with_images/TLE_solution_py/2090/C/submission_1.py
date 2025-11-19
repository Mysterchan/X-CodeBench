def main():
    import sys, heapq
    data = sys.stdin.read().strip().split()
    if not data:
        return
    q = int(data[0])
    pos = 1
    BOUND = 320
    table_status = {}
    for i in range(BOUND + 1):
        for j in range(BOUND - i + 1):
            table_status[(i, j)] = 0
    cand_list = []
    for (i, j) in table_status.keys():
        base = 3 * (i + j)
        xA, yA = 3 * i + 1, 3 * j + 1
        cand_list.append((base + 2, xA, yA, i, j, 0))
        xB, yB = 3 * i + 1, 3 * j + 2
        cand_list.append((base + 3, xB, yB, i, j, 1))
        xC, yC = 3 * i + 2, 3 * j + 1
        cand_list.append((base + 3, xC, yC, i, j, 2))
        xD, yD = 3 * i + 2, 3 * j + 2
        cand_list.append((base + 6, xD, yD, i, j, 3))
    cand_list.sort(key=lambda tup: (tup[0], tup[1], tup[2]))

    avail_tables = []
    for (i, j) in table_status.keys():
        key = (3 * (i + j) + 2, 3 * i + 1, 3 * j + 1, i, j)
        heapq.heappush(avail_tables, key)

    out_lines = []
    for _ in range(q):
        n = int(data[pos])
        pos += 1
        guest_types = list(map(int, data[pos: pos + n]))
        pos += n
        cur_table_status = {k: 0 for k in table_status.keys()}
        cur_avail = avail_tables[:]
        heapq.heapify(cur_avail)
        cand_ptr = 0
        for gt in guest_types:
            if gt == 1:
                while cand_ptr < len(cand_list):
                    d, cx, cy, ti, tj, seat_type = cand_list[cand_ptr]
                    mask = 1 << seat_type
                    if (cur_table_status[(ti, tj)] & mask) != 0:
                        cand_ptr += 1
                        continue
                    break
                d, cx, cy, ti, tj, seat_type = cand_list[cand_ptr]
                cand_ptr += 1
                cur_table_status[(ti, tj)] |= (1 << seat_type)
                out_lines.append(f"{cx} {cy}")
            else:
                while cur_avail:
                    key = cur_avail[0]
                    _, ax, ay, ti, tj = key
                    if cur_table_status[(ti, tj)] == 0:
                        break
                    else:
                        heapq.heappop(cur_avail)
                if not cur_avail:
                    while cand_ptr < len(cand_list):
                        d, cx, cy, ti, tj, seat_type = cand_list[cand_ptr]
                        mask = 1 << seat_type
                        if (cur_table_status[(ti, tj)] & mask) != 0:
                            cand_ptr += 1
                            continue
                        break
                    d, cx, cy, ti, tj, seat_type = cand_list[cand_ptr]
                    cand_ptr += 1
                    cur_table_status[(ti, tj)] |= (1 << seat_type)
                    out_lines.append(f"{cx} {cy}")
                else:
                    key = heapq.heappop(cur_avail)
                    _, ax, ay, ti, tj = key
                    seat_type = 0
                    cur_table_status[(ti, tj)] |= (1 << seat_type)
                    out_lines.append(f"{ax} {ay}")

    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
