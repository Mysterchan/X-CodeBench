A = list(map(int, input().split()))

# 检查交换每对相邻元素后是否能得到升序序列
target = [1, 2, 3, 4, 5]

for i in range(4):
    # 创建副本并交换相邻元素
    B = A[:]
    B[i], B[i+1] = B[i+1], B[i]
    
    # 检查是否为升序
    if B == target:
        print("Yes")
        exit()

print("No")