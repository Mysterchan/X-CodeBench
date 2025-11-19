import sys
from math import inf

fib = [0] * 11
fib[1] = 1
fib[2] = 2
for i in range(3, 11):
    fib[i] = fib[i-1] + fib[i-2]

max_dim = 150
H_min = [[[inf] * (max_dim + 1) for _ in range(max_dim + 1)] for __ in range(11)]

def compute_h_min(n, W, L):
    C = [fib[k] for k in range(n, 0, -1)]
    largest = C[0]
    if W < largest or L < largest:
        return inf
    slots = [(0, 0, W, L, 0)]

    for s in C:
        slots.sort(key=lambda x: (x[4], x[0], x[1]))
        selected = None
        for slot in slots:
            x, y, w_slot, l_slot, h_slot = slot
            if w_slot >= s and l_slot >= s:
                selected = slot
                break
        if selected is None:
            return inf

        x, y, w_slot, l_slot, h_slot = selected
        slots.remove(selected)
        if w_slot > s:
            slots.append((x + s, y, w_slot - s, s, h_slot))
        if l_slot > s:
            slots.append((x, y + s, w_slot, l_slot - s, h_slot))
        slots.append((x, y, s, s, h_slot + s))

    return max(slot[4] for slot in slots)

for n in range(2, 11):
    for W in range(1, max_dim + 1):
        for L in range(W, max_dim + 1):
            height = compute_h_min(n, W, L)
            H_min[n][W][L] = height
            H_min[n][L][W] = height

def main():
    input_data = sys.stdin.read().split()
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr + 1])
        ptr += 2
        result = []
        for __ in range(m):
            w = int(input_data[ptr])
            l = int(input_data[ptr + 1])
            h = int(input_data[ptr + 2])
            ptr += 3
            valid = False
            if H_min[n][l][h] <= w:
                valid = True
            elif H_min[n][w][h] <= l:
                valid = True
            elif H_min[n][w][l] <= h:
                valid = True
            result.append('1' if valid else '0')
        print(''.join(result))

if __name__ == "__main__":
    main()
