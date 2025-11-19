def solve():
    MOD = 998244353
    N = int(input())
    S = input().strip()
    
    # BFSで到達可能な全ての状態を探索
    from collections import deque
    
    visited = {S}
    queue = deque([S])
    
    while queue:
        current = queue.popleft()
        
        # 全ての正しい括弧列の部分文字列を見つける
        n = len(current)
        for l in range(n):
            depth = 0
            for r in range(l, n):
                if current[r] == '(':
                    depth += 1
                else:
                    depth -= 1
                
                # depth == 0 なら l から r までが正しい括弧列
                if depth == 0:
                    # 反転操作を適用
                    new_s = list(current)
                    for i in range(l, r + 1):
                        j = l + r - i
                        if current[j] == '(':
                            new_s[i] = ')'
                        else:
                            new_s[i] = '('
                    new_s = ''.join(new_s)
                    
                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append(new_s)
    
    print(len(visited))

solve()