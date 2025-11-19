def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    # 各要素が目的位置に到達するまでのコストを計算
    total_cost = 0
    
    # 各要素について、現在位置から目的位置への移動コストを計算
    for i in range(n):
        # p[i]の値は、インデックスp[i]-1に移動する必要がある
        target = p[i] - 1
        current = i
        
        if current > target:
            # 左に移動する必要がある
            # currentからtargetまでの各位置のコストの合計
            for j in range(target, current):
                total_cost += j + 1
    
    print(total_cost)

solve()