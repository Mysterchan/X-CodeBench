def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    edges_seen = set()
    remove_count = 0

    for _ in range(M):
        u, v = map(int, input().split())
        if u == v:
            # self-loop, must remove
            remove_count += 1
        else:
            # store edges in sorted order to detect multi-edges
            edge = (min(u, v), max(u, v))
            if edge in edges_seen:
                # multi-edge, must remove
                remove_count += 1
            else:
                edges_seen.add(edge)

    print(remove_count)

if __name__ == "__main__":
    main()