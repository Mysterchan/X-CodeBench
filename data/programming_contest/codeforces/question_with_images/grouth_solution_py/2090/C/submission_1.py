import sys
from collections import defaultdict

def main():
    D_max = 600
    A = []
    for i in range(0, 200):
        for j in range(0, 200):
            for (dx, dy) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
                a = 3 * i + dx
                b = 3 * j + dy
                if dx == 1 and dy == 1:
                    g = 2
                elif (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
                    g = 3
                else:
                    g = 6
                d = 3 * (i + j) + g
                if d <= D_max:
                    A.append((d, a, b, i, j))
    A.sort(key=lambda x: (x[0], x[1], x[2]))

    data = sys.stdin.read().split()
    q = int(data[0])
    index = 1
    output_lines = []
    for _ in range(q):
        n = int(data[index]); index += 1
        t_list = list(map(int, data[index:index+n]))
        index += n

        ptr1 = 0
        ptr0 = 0
        occupied = [False] * len(A)
        table_count = defaultdict(int)
        res = []

        for ti in t_list:
            if ti == 1:
                while ptr1 < len(A):
                    d_val, a_val, b_val, i_val, j_val = A[ptr1]
                    if not occupied[ptr1]:
                        break
                    ptr1 += 1
                if ptr1 < len(A):
                    occupied[ptr1] = True
                    table_count[(i_val, j_val)] += 1
                    ptr1 += 1
                    res.append(f"{a_val} {b_val}")
                else:
                    res.append("0 0")
            else:
                while ptr0 < len(A):
                    d_val, a_val, b_val, i_val, j_val = A[ptr0]
                    if not occupied[ptr0] and table_count.get((i_val, j_val), 0) == 0:
                        break
                    ptr0 += 1
                if ptr0 < len(A):
                    occupied[ptr0] = True
                    table_count[(i_val, j_val)] = 1
                    ptr0 += 1
                    res.append(f"{a_val} {b_val}")
                else:
                    res.append("0 0")
        output_lines.extend(res)

    print("\n".join(output_lines))

if __name__ == "__main__":
    main()
