import sys
import threading

def main():
    import sys
    data = sys.stdin.readline
    N, M = map(int, data().split())
    removals = 0
    keys = []
    for _ in range(M):
        u, v = map(int, data().split())
        if u == v:
            # self-loop must be removed
            removals += 1
        else:
            # encode unordered pair (min, max) into one integer
            if u > v:
                u, v = v, u
            keys.append((u << 32) | v)

    # sort to group duplicates
    keys.sort()

    # count parallel edges
    prev = -1
    count = 0
    for key in keys:
        if key != prev:
            # finalize the previous group
            if count > 1:
                removals += count - 1
            prev = key
            count = 1
        else:
            count += 1

    # finalize last group
    if count > 1:
        removals += count - 1

    print(removals)

if __name__ == "__main__":
    main()