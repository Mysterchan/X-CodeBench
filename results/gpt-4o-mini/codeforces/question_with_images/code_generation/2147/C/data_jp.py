def can_arrange_rabbits(t, test_cases):
    results = []
    for n, s in test_cases:
        if '11' in s:
            results.append("NO")
        else:
            results.append("YES")
    return results

# 入力の読み込み
import sys
input = sys.stdin.read
data = input().strip().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n = int(data[index])
    s = data[index + 1]
    test_cases.append((n, s))
    index += 2

# 結果の出力
results = can_arrange_rabbits(t, test_cases)
print("\n".join(results))