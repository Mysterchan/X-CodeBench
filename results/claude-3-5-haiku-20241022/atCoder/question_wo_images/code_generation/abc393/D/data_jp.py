N = int(input())
S = input()

# すべての1の位置を取得
ones = [i for i in range(N) if S[i] == '1']
k = len(ones)

# すべての1を連続した区間に集める
# 最適な区間の位置を探す
# 区間[l, l+k-1]にすべての1を集めるとき、
# 各1がその区間内の位置に移動するコストを最小化する

min_cost = float('inf')

# 可能なすべての連続区間を試す
for start in range(N - k + 1):
    # 区間[start, start+k-1]に1を集める
    # ones[j]番目の1を、start+j番目の位置に移動させる
    cost = 0
    for j in range(k):
        cost += abs(ones[j] - (start + j))
    min_cost = min(min_cost, cost)

print(min_cost)