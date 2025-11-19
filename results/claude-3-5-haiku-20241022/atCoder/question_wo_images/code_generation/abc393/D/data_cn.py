N = int(input())
S = input()

# 统计1的个数
count_ones = S.count('1')

# 如果所有字符都是1，不需要交换
if count_ones == N:
    print(0)
else:
    # 滑动窗口找到包含最多1的长度为count_ones的子串
    # 也就是找到包含最少0的窗口
    min_zeros = float('inf')
    
    # 初始化第一个窗口
    zeros_in_window = S[:count_ones].count('0')
    min_zeros = zeros_in_window
    
    # 滑动窗口
    for i in range(1, N - count_ones + 1):
        # 移除左边的字符，添加右边的字符
        if S[i-1] == '0':
            zeros_in_window -= 1
        if S[i+count_ones-1] == '0':
            zeros_in_window += 1
        
        min_zeros = min(min_zeros, zeros_in_window)
    
    print(min_zeros)