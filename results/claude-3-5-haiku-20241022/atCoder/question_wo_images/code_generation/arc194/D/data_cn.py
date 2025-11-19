def solve():
    MOD = 998244353
    N = int(input())
    S = input().strip()
    
    # 使用BFS找到所有可达的状态
    from collections import deque
    
    visited = set()
    queue = deque()
    queue.append(S)
    visited.add(S)
    
    while queue:
        current = queue.popleft()
        
        # 尝试所有可能的有效括号子序列并反转
        n = len(current)
        for l in range(n):
            for r in range(l + 1, n + 1):
                substring = current[l:r]
                if is_valid(substring):
                    # 执行反转操作
                    new_string = current[:l] + reverse_special(substring) + current[r:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)
    
    print(len(visited) % MOD)

def is_valid(s):
    """检查字符串是否为有效括号序列"""
    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False
    
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    
    return balance == 0

def reverse_special(s):
    """执行特殊的反转操作"""
    result = []
    for char in reversed(s):
        if char == '(':
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)

solve()