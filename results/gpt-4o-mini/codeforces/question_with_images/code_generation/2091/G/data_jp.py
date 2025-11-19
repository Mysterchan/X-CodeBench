t = int(input())
results = []

for _ in range(t):
    s, k = map(int, input().split())
    
    # 戻らずにsに到達するために必要な力
    # 戻ることを最大限に活用する
    power_left = k
    
    while power_left > 0:
        if s <= power_left:
            # そのまま進む場合
            results.append(power_left)
            break
        
        # s - power_left > 0 ならば、戻らなければならない
        s -= power_left
        power_left -= 1

    else:
        # パワーがなくなる場合
        results.append(max(0, power_left))
        
print("\n".join(map(str, results)))