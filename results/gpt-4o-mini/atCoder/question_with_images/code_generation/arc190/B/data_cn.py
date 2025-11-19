def compute_ways(N, a, b, Q, ks):
    MOD = 998244353
    
    results = []
    for k in ks:
        # 对于一个 K 级 L 形状，能够包含单元格 (a, b) 的条件
        if k > a or k > b or k > (N - a + 1) or k > (N - b + 1):
            results.append(0)
            continue
        
        # 计算可能的方式
        # 每个方向都有两种选择，前面和后面分别可以选取 k 和 k - 1 个单元格的排列方式
        ways = (k * (N - k + 1)) % MOD
        results.append(ways)

    return results

# 读取输入
import sys
input_data = sys.stdin.read().split()
N = int(input_data[0])
a = int(input_data[1])
b = int(input_data[2])
Q = int(input_data[3])
ks = list(map(int, input_data[4:4 + Q]))

# 计算结果
results = compute_ways(N, a, b, Q, ks)

# 输出结果
sys.stdout.write('\n'.join(map(str, results)) + '\n')