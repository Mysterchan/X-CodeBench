def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 各袋の石を他の袋に移す操作を考える
    # 最終的に各袋に入っている石の数は、元の石の数の部分和になる
    # ただし、全体の和は常に sum(A) に等しい
    
    # 袋iの最終的な石の数をB_iとすると、
    # B_i は A の部分集合の和（袋iに移された石たち）になる
    # 制約: sum(B_i) = sum(A)
    
    total = sum(A)
    
    # 可能な部分和の集合を求める
    possible_sums = {0}
    for a in A:
        new_sums = set()
        for s in possible_sums:
            new_sums.add(s + a)
        possible_sums.update(new_sums)
    
    # 各袋に割り当て可能な石の数の組み合わせを全探索
    # ただし、XORの値だけを追跡する
    
    # dp[mask] = maskで表される袋の部分集合に石を割り当てた時に
    # 可能なXOR値の集合
    # ただし、これは指数的に大きくなる可能性がある
    
    # 別のアプローチ: 各袋に何個の石を入れるかを決める
    # N個の非負整数 B_1, ..., B_N で sum(B_i) = total かつ
    # 各B_iが可能な部分和に含まれるもの
    
    # N=12なので、動的計画法を使う
    # dp[i][xor_val] = i番目の袋まで見て、XORがxor_valになる場合に
    # 使った石の総数の集合
    
    from collections import defaultdict
    
    # dp[xor_val] = このXOR値を達成するために使った石の総数の集合
    dp = defaultdict(set)
    dp[0].add(0)
    
    for i in range(N):
        new_dp = defaultdict(set)
        for xor_val, sums in dp.items():
            for s in sums:
                # 袋iに何も入れない（実質的に0を入れる）
                new_xor = xor_val ^ 0
                new_dp[new_xor].add(s)
                
                # 袋iに可能な部分和を入れる
                for subset_sum in possible_sums:
                    if subset_sum > 0 and s + subset_sum <= total:
                        new_xor = xor_val ^ subset_sum
                        new_dp[new_xor].add(s + subset_sum)
        dp = new_dp
    
    # sum = total となるXOR値を収集
    result = set()
    for xor_val, sums in dp.items():
        if total in sums:
            result.add(xor_val)
    
    print(len(result))

solve()