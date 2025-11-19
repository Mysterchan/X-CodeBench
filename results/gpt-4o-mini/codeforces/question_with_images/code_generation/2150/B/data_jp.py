MOD = 998244353

def count_valid_grids(n, a):
    total_black_cells = sum(a)
    if total_black_cells != n:  # 必要な黒いセルの数がnでなければ無効
        return 0

    # 必要な黒いセルが各行に正しく配置できるかのチェック
    for i in range(n):
        if a[i] > n - i:  # 行に必要な黒いセル数が残りの列数を超えてはいけない
            return 0

    # 有効なグリッドの組み合わせ数
    count = 1
    available_spaces = n
    # セルの配置を行ごとに計算
    for k in range(1, n + 1):
        count *= available_spaces
        count %= MOD
        available_spaces -= a[k - 1]  # 次の行に使えるスペースを減らす
    
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        result = count_valid_grids(n, a)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()