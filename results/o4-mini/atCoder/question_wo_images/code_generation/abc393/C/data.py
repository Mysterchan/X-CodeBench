import sys
import threading

def main():
    import sys

    data = sys.stdin
    line = data.readline().split()
    if not line:
        print(0)
        return
    n = int(line[0])
    m = int(line[1])

    removals = 0
    counts = {}

    for _ in range(m):
        u, v = map(int, data.readline().split())

        # Self-loop case
        if u == v:
            removals += 1
            continue

        # Order the pair so that (u, v) == (v, u)
        if u > v:
            u, v = v, u

        key = (u, v)
        c = counts.get(key, 0)
        if c >= 1:
            # We've already seen this edge once, so any extra is a removal
            removals += 1
        counts[key] = c + 1

    print(removals)

if __name__ == "__main__":
    main()