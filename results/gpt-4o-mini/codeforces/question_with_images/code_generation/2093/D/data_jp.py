def fill_table(n):
    size = 2 ** n
    table = [[0] * size for _ in range(size)]
    
    def fill(r1, r2, c1, c2, num):
        if r2 - r1 == 2 and c2 - c1 == 2:
            table[r1][c1] = num
            table[r1][c2 - 1] = num + 1
            table[r2 - 1][c1] = num + 2
            table[r2 - 1][c2 - 1] = num + 3
            return num + 4
        mid_r = (r1 + r2) // 2
        mid_c = (c1 + c2) // 2
        num = fill(r1, mid_r, c1, mid_c, num)
        num = fill(r1, mid_r, mid_c, c2, num)
        num = fill(mid_r, r2, c1, mid_c, num)
        num = fill(mid_r, r2, mid_c, c2, num)
        return num
    
    fill(0, size, 0, size, 1)
    return table

def find_value(table, x, y):
    return table[x - 1][y - 1]

def find_coordinates(n, d):
    size = 2 ** n
    r1, r2, c1, c2 = 0, size, 0, size
    num = 1
    
    while r1 < r2:
        if d == num:
            return r1 + 1, c1 + 1
        
        mid_r = (r1 + r2) // 2
        mid_c = (c1 + c2) // 2
        
        if r1 < mid_r and c1 < mid_c:
            # Top-left
            num += 1
            r2 = mid_r
            c2 = mid_c
        elif r1 < mid_r and mid_c <= c2:
            # Top-right
            num += (mid_r - r1) * (mid_c - c1)
            r2 = mid_r
            c1 = mid_c
        elif mid_r <= r2 and c1 < mid_c:
            # Bottom-left
            num += (mid_r - r1) * (mid_c - c1)
            num += 1
            r1 = mid_r
            c2 = mid_c
        else: # mid_r <= r2 and mid_c <= c2
            # Bottom-right
            num += (mid_r - r1) * (mid_c - c1)
            num += 1
            num += (mid_r - r1) * (mid_c - c1)
            r1 = mid_r
            c1 = mid_c
    
    return -1, -1

import sys
input = sys.stdin.read

data = input().splitlines()
index = 0
t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    queries = int(data[index])
    index += 1
    
    table = fill_table(n)
    
    for __ in range(queries):
        query = data[index].split()
        index += 1
        
        if query[0] == "->":
            x = int(query[1])
            y = int(query[2])
            results.append(str(find_value(table, x, y)))
        else:
            d = int(query[1])
            x, y = find_coordinates(n, d)
            results.append(f"{x} {y}")

print("\n".join(results))