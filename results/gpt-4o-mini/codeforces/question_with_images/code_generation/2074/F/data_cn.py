def count_quadtree_nodes(l1, r1, l2, r2):
    def count_nodes(x1, x2, y1, y2):
        if x1 >= x2 or y1 >= y2:
            return 0
        size = max(x2 - x1, y2 - y1)
        if size == 1:
            return 1
        half_size = size // 2
        return (count_nodes(x1, x1 + half_size, y1, y1 + half_size) +
                count_nodes(x1 + half_size, x2, y1, y1 + half_size) +
                count_nodes(x1, x1 + half_size, y1 + half_size, y2) +
                count_nodes(x1 + half_size, x2, y1 + half_size, y2))

    return count_nodes(l1, r1, l2, r2)

t = int(input())
results = []
for _ in range(t):
    l1, r1, l2, r2 = map(int, input().split())
    results.append(count_quadtree_nodes(l1, r1, l2, r2))

print('\n'.join(map(str, results)))