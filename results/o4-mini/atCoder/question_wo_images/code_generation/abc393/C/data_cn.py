import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    remove_count = 0
    edge_counts = {}

    for _ in range(M):
        u, v = map(int, input().split())
        if u == v:
            # Self-loop must be removed
            remove_count += 1
        else:
            # Normalize order for undirected edge
            if u > v:
                u, v = v, u
            key = (u, v)
            edge_counts[key] = edge_counts.get(key, 0) + 1

    # For each multi-edge group, keep one and remove the rest
    for cnt in edge_counts.values():
        if cnt > 1:
            remove_count += cnt - 1

    print(remove_count)

if __name__ == "__main__":
    main()