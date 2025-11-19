n = int(input())
a = list(map(int, input().split()))

results = set()

for l in range(n):
    # 对于每个起始位置L
    current = a.copy()
    for r in range(l, n):
        # 将位置r的元素替换为a[l]
        current[r] = a[l]
        # 记录当前序列
        results.add(tuple(current))

print(len(results))