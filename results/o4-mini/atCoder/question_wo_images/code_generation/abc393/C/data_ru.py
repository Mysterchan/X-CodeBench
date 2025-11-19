#!/usr/bin/env python3
import sys
import threading
def main():
    data = sys.stdin
    first = data.readline().split()
    if not first:
        return
    n = int(first[0]); m = int(first[1])
    loops = 0
    edge_count = {}
    for _ in range(m):
        u, v = map(int, data.readline().split())
        if u == v:
            loops += 1
        else:
            if u > v:
                u, v = v, u
            key = (u, v)
            edge_count[key] = edge_count.get(key, 0) + 1
    removals = loops
    for cnt in edge_count.values():
        if cnt > 1:
            removals += cnt - 1
    print(removals)

if __name__ == "__main__":
    main()