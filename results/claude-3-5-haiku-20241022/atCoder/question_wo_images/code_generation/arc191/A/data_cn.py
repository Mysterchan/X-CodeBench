def solve():
    N, M = map(int, input().split())
    S = list(input().strip())
    T = input().strip()
    
    # 贪心策略：对于每个操作，尝试从左到右找到第一个可以被提升的位置
    for k in range(M):
        char_t = T[k]
        # 从左到右找到第一个小于char_t的位置进行替换
        replaced = False
        for i in range(N):
            if S[i] < char_t:
                S[i] = char_t
                replaced = True
                break
        
        # 如果没有找到可以提升的位置，替换最后一个位置
        if not replaced:
            S[N - 1] = char_t
    
    print(''.join(S))

solve()