import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    edge_count = {}
    to_remove = 0

    for _ in range(M):
        u, v = map(int, input().split())
        if u == v:
            # Loop edge, must remove
            to_remove += 1
        else:
            # Sort vertices to handle undirected edge uniquely
            a, b = (u, v) if u < v else (v, u)
            if (a, b) in edge_count:
                # Multiple edge found, must remove this one
                to_remove += 1
            else:
                edge_count[(a, b)] = 1

    print(to_remove)

if __name__ == "__main__":
    main()