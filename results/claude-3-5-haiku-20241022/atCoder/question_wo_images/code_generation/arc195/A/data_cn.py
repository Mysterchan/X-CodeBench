def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 找出所有可能匹配B的起始位置
    # dp[i][j] = 從A[i:]開始匹配B[j:]的方式數
    
    # 我們需要計算有多少種方式可以在A中找到B的子序列
    # 如果有至少2種方式，輸出Yes
    
    # 使用動態規劃計算子序列匹配數
    # count[i][j] = 從A的前i個元素中匹配B的前j個元素的方式數
    
    count = [[0] * (M + 1) for _ in range(N + 1)]
    
    # 初始化：匹配空序列只有一種方式
    for i in range(N + 1):
        count[i][0] = 1
    
    # 動態規劃
    for i in range(1, N + 1):
        for j in range(M + 1):
            # 不使用A[i-1]
            count[i][j] = count[i-1][j]
            
            # 使用A[i-1]（如果匹配）
            if j > 0 and A[i-1] == B[j-1]:
                count[i][j] += count[i-1][j-1]
                
                # 為了避免數字過大，如果已經>=2就可以提前結束
                if count[i][j] >= 2:
                    count[i][j] = 2
    
    if count[N][M] >= 2:
        print("Yes")
    else:
        print("No")

solve()