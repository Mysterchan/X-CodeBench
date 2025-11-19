import bisect

def max_items_for_budget(prices, budget):
    # 各商品について、予算内で買える最大個数を計算
    max_buyable = []
    for p in prices:
        # k^2 * p <= budget
        # k <= sqrt(budget / p)
        k = int((budget / p) ** 0.5)
        # 浮動小数点誤差を考慮して確認
        while k * k * p <= budget:
            k += 1
        k -= 1
        if k > 0:
            max_buyable.append((p, k))
    
    if not max_buyable:
        return 0
    
    # 価格でソート
    max_buyable.sort()
    
    # 二分探索で答えを求める
    def can_buy(total_items):
        # total_items個を買えるか判定
        cost = 0
        remaining = total_items
        
        for p, max_k in max_buyable:
            if remaining == 0:
                break
            # この商品から買う個数
            buy = min(remaining, max_k)
            cost += buy * buy * p
            if cost > budget:
                return False
            remaining -= buy
        
        return remaining == 0
    
    # 最大購入可能個数の上限を計算
    max_possible = sum(k for _, k in max_buyable)
    
    left, right = 0, max_possible
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_buy(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer

# 入力を読み込む
N, M = map(int, input().split())
P = list(map(int, input().split()))

# 答えを計算して出力
print(max_items_for_budget(P, M))