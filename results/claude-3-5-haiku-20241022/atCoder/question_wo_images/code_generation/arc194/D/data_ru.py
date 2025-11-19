def solve():
    MOD = 998244353
    N = int(input())
    S = input().strip()
    
    # Преобразуем строку в последовательность балансов
    def to_balance(s):
        balance = []
        curr = 0
        for c in s:
            if c == '(':
                curr += 1
            else:
                curr -= 1
            balance.append(curr)
        return tuple(balance)
    
    # Проверка валидности последовательности скобок
    def is_valid(s):
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    # Применяем операцию разворота
    def reverse_operation(s, l, r):
        s_list = list(s)
        for i in range(l, r + 1):
            original_pos = l + r - i
            if s[original_pos] == '(':
                s_list[i] = ')'
            else:
                s_list[i] = '('
        return ''.join(s_list)
    
    # BFS для поиска всех достижимых состояний
    visited = set()
    queue = [S]
    visited.add(S)
    
    while queue:
        current = queue.pop(0)
        
        # Пробуем все возможные подстроки
        for l in range(N):
            for r in range(l, N):
                substring = current[l:r+1]
                if is_valid(substring):
                    new_s = reverse_operation(current, l, r)
                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append(new_s)
    
    print(len(visited) % MOD)

solve()