def can_sort_with_one_swap(a):
    # 確認のための昇順配列
    sorted_a = sorted(a)
    
    # 不一致のインデックスを収集
    mismatch_indices = [i for i in range(5) if a[i] != sorted_a[i]]
    
    # 1つの操作で整列できる条件
    if len(mismatch_indices) == 2:
        # 2つの不一致が隣接している場合
        return 'Yes'
    else:
        return 'No'

# 入力の取得
A = list(map(int, input().strip().split()))

# 出力
print(can_sort_with_one_swap(A))