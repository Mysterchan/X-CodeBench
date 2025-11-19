n = int(input())
p = list(map(int, input().split()))

total_cost = 0

# 对于每个位置，如果元素不在正确位置，需要移动
for i in range(n):
    # 找到数字 i+1 应该在的位置
    target_val = i + 1
    current_pos = p.index(target_val)
    
    # 将 target_val 从 current_pos 移动到位置 i
    while current_pos > i:
        # 交换 p[current_pos-1] 和 p[current_pos]
        # 成本是 current_pos（因为是交换位置 current_pos-1 和 current_pos，索引从0开始，题目中从1开始）
        total_cost += current_pos
        p[current_pos-1], p[current_pos] = p[current_pos], p[current_pos-1]
        current_pos -= 1

print(total_cost)