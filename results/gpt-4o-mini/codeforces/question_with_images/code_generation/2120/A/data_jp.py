def can_form_square(l1, b1, l2, b2, l3, b3):
    # 長方形の合計高さと最大幅を計算
    total_height = b1 + b2 + b3
    max_width = max(l1, l2, l3)
    
    # 高さと幅が一致するかチェック
    if total_height == max_width:
        return "YES"
    return "NO"

t = int(input())
results = []
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    results.append(can_form_square(l1, b1, l2, b2, l3, b3))

print("\n".join(results))