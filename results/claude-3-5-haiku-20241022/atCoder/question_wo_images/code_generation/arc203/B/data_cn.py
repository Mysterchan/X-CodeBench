def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        
        # 首先检查两个序列的和是否相等
        if sum(A) != sum(B):
            print("No")
            continue
        
        # 构建所有可能的子序列（按其和分类）
        # 对于每个和值，存储所有可能的子序列长度
        def get_all_subarrays(arr):
            # 返回一个字典，键是子序列的和，值是该和对应的所有子序列长度的多重集
            from collections import defaultdict
            sums_to_lengths = defaultdict(list)
            n = len(arr)
            for i in range(n):
                current_sum = 0
                for j in range(i, n):
                    current_sum += arr[j]
                    sums_to_lengths[current_sum].append(j - i + 1)
            return sums_to_lengths
        
        a_subarrays = get_all_subarrays(A)
        b_subarrays = get_all_subarrays(B)
        
        # 检查关键不变量：对于每个可能的和，在A中可以形成的子序列长度集合
        # 必须能覆盖B中需要的子序列长度集合
        
        # 实际上，我们需要用BFS/DFS来检查是否能从A变换到B
        # 但这可能太复杂。让我们用另一个思路：
        # 关键观察：操作保留了什么不变量？
        
        # 让我们用状态空间搜索（由于N小，可能可行）
        from collections import deque
        
        def to_tuple(arr):
            return tuple(arr)
        
        visited = set()
        queue = deque([A[:]])
        visited.add(to_tuple(A))
        target = to_tuple(B)
        found = False
        
        if to_tuple(A) == target:
            print("Yes")
            continue
        
        # 限制搜索深度和状态数
        max_states = 100000
        
        while queue and len(visited) < max_states:
            current = queue.popleft()
            
            # 尝试所有可能的操作
            n = len(current)
            for a in range(n):
                sum_a = 0
                for b in range(a, n):
                    sum_a += current[b]
                    for c in range(b + 1, n):
                        sum_c = 0
                        for d in range(c, n):
                            sum_c += current[d]
                            if sum_a == sum_c:
                                # 执行交换操作
                                new_arr = current[:a] + current[c:d+1] + current[b+1:c] + current[a:b+1] + current[d+1:]
                                new_tuple = to_tuple(new_arr)
                                
                                if new_tuple == target:
                                    found = True
                                    break
                                
                                if new_tuple not in visited:
                                    visited.add(new_tuple)
                                    queue.append(new_arr)
                        
                        if found:
                            break
                    
                    if found:
                        break
                
                if found:
                    break
            
            if found:
                break
        
        if found:
            print("Yes")
        else:
            print("No")

solve()