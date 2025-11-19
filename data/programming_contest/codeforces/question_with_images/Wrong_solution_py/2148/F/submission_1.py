import sys

def main():
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    t = int(data[ptr])
    ptr += 1
    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        rows = []
        for __ in range(n):
            k = int(data[ptr])
            ptr += 1
            row = list(map(int, data[ptr:ptr + k]))
            ptr += k
            rows.append(row)
        rows.sort(reverse=True)
        current_max = 0
        res = []
        for row in reversed(rows):
            l = len(row)
            if l > current_max:
                res.extend(row[current_max:])
                current_max = l
        print(' '.join(map(str, res)) + ' ')

if __name__ == "__main__":
    main()
