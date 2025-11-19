def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    if N == 1:
        print(0)
        return
    
    # dp[l][r][0/1] = 区間[l, r]を処理した時の最大スコア
    # 最後の要素: 0 = 左端が残っている, 1 = 右端が残っている
    # dp[l][r][2] = 区間[l, r]が全て削除された時の最大スコア
    
    dp = {}
    
    def rec(l, r):
        if l > r:
            return (0, -1)  # (スコア, 残っている要素のインデックス or -1)
        if l == r:
            return (0, l)  # (スコア, 残っている要素のインデックス)
        
        if (l, r) in dp:
            return dp[(l, r)]
        
        best_score = -1
        best_remaining = -1
        
        # 全ての分割方法を試す
        # 左側を完全に削除、右側を完全に削除
        left_result = rec(l+1, r)
        if left_result[1] == -1:
            # 右側が全て削除された場合、左端が残る
            best_score = left_result[0]
            best_remaining = l
        else:
            # 右側に要素が残っている場合、左端とペアにできる
            score = left_result[0] + abs(A[l] - A[left_result[1]])
            if score > best_score:
                best_score = score
                best_remaining = -1
        
        right_result = rec(l, r-1)
        if right_result[1] == -1:
            # 左側が全て削除された場合、右端が残る
            if right_result[0] > best_score or (right_result[0] == best_score and best_remaining == -1):
                best_score = right_result[0]
                best_remaining = r
        else:
            # 左側に要素が残っている場合、右端とペアにできる
            score = right_result[0] + abs(A[r] - A[right_result[1]])
            if score > best_score:
                best_score = score
                best_remaining = -1
        
        # 中間で分割
        for mid in range(l, r):
            left_result = rec(l, mid)
            right_result = rec(mid+1, r)
            
            if left_result[1] == -1 and right_result[1] == -1:
                # 両方とも完全に削除
                score = left_result[0] + right_result[0]
                if score > best_score:
                    best_score = score
                    best_remaining = -1
            elif left_result[1] != -1 and right_result[1] == -1:
                # 左側に残り、右側は完全削除
                score = left_result[0] + right_result[0]
                if score > best_score:
                    best_score = score
                    best_remaining = left_result[1]
            elif left_result[1] == -1 and right_result[1] != -1:
                # 左側は完全削除、右側に残り
                score = left_result[0] + right_result[0]
                if score > best_score:
                    best_score = score
                    best_remaining = right_result[1]
            else:
                # 両方に残りがある場合、ペアにする
                score = left_result[0] + right_result[0] + abs(A[left_result[1]] - A[right_result[1]])
                if score > best_score:
                    best_score = score
                    best_remaining = -1
        
        dp[(l, r)] = (best_score, best_remaining)
        return dp[(l, r)]
    
    result = rec(0, N-1)
    print(result[0])

solve()