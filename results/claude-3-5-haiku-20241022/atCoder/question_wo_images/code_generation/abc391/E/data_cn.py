def solve():
    N = int(input())
    A = input().strip()
    
    # 計算當前結果
    def compute(s):
        while len(s) > 1:
            new_s = []
            for i in range(0, len(s), 3):
                group = s[i:i+3]
                count = sum(int(c) for c in group)
                new_s.append('1' if count >= 2 else '0')
            s = ''.join(new_s)
        return s[0]
    
    current_result = compute(A)
    target = '0' if current_result == '1' else '1'
    
    # 動態規劃：計算將字串段變成目標值所需的最小更改數
    def min_changes(s, target_val):
        n = len(s)
        if n == 1:
            return 0 if s == target_val else 1
        
        # memo[pos][length][target] = 最小更改數
        memo = {}
        
        def dp(pos, length, tgt):
            if length == 1:
                return 0 if s[pos] == tgt else 1
            
            if (pos, length, tgt) in memo:
                return memo[(pos, length, tgt)]
            
            result = float('inf')
            step = length // 3
            
            # 枚舉三個子段的目標值組合
            for v1 in ['0', '1']:
                for v2 in ['0', '1']:
                    for v3 in ['0', '1']:
                        # 檢查多數值是否等於目標
                        count = int(v1) + int(v2) + int(v3)
                        majority = '1' if count >= 2 else '0'
                        
                        if majority == tgt:
                            cost = dp(pos, step, v1) + dp(pos + step, step, v2) + dp(pos + 2*step, step, v3)
                            result = min(result, cost)
            
            memo[(pos, length, tgt)] = result
            return result
        
        return dp(0, n, target_val)
    
    print(min_changes(A, target))

solve()