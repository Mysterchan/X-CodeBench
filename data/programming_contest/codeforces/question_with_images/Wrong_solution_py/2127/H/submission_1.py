import random
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        m = int(data[index+1])
        index += 2
        edges = []
        for i in range(m):
            u = int(data[index]) - 1
            v = int(data[index+1]) - 1
            index += 2
            edges.append((u, v))

        best_count = 0
        if m == 0:
            results.append("0")
            continue

        for it in range(100):
            random.shuffle(edges)
            degree = [0] * n
            count = 0
            for (u, v) in edges:
                if degree[u] < 2 and degree[v] < 2:
                    count += 1
                    degree[u] += 1
                    degree[v] += 1
            if count > best_count:
                best_count = count

        results.append(str(best_count))

    print("\n".join(results))

if __name__ == "__main__":
    main()
