def process_case(n, rows):
    from collections import defaultdict
    import heapq

    # 创建一个优先队列（大根堆）用于每一列的状态
    columns = defaultdict(list)
    
    # 将每一行的元素加入到对应的列中
    for row in rows:
        for col_index in range(len(row)):
            heapq.heappush(columns[col_index], -row[col_index])  # 使用负数模拟大根堆

    # 计算最终底行
    final_row = []
    for i in range(len(columns)):
        if columns[i]:
            final_row.append(-heapq.heappop(columns[i]))  # 取得当前列的最大值

    return sorted(final_row)  # 字典序最小需要排序

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    rows = []
    for _ in range(n):
        data = list(map(int, input().split()))
        k_i = data[0]
        array = data[1:k_i + 1]
        rows.append(array)
    
    result = process_case(n, rows)
    results.append(" ".join(map(str, result)))

# 输出所有结果
print("\n".join(results))