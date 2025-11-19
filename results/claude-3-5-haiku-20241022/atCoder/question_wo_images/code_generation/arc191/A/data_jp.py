N, M = map(int, input().split())
S = list(input().strip())
T = input().strip()

for k in range(M):
    t_char = T[k]
    
    # 最も左の位置で、t_charに置き換えることで値が増加する位置を探す
    best_pos = -1
    for i in range(N):
        if S[i] < t_char:
            best_pos = i
            break
    
    # 置き換えることで値が増加する位置が見つかった場合
    if best_pos != -1:
        S[best_pos] = t_char
    else:
        # 増加する位置がない場合、最も右の位置で最小の数字を置き換える
        min_pos = N - 1
        for i in range(N - 1, -1, -1):
            if S[i] <= S[min_pos]:
                min_pos = i
        S[min_pos] = t_char

print(''.join(S))