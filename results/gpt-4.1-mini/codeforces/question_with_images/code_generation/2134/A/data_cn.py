t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    # 根據題意和示例分析：
    # 若 a + b > n + 1，則無法形成對稱的著色，輸出 NO
    # 否則輸出 YES
    print("YES" if a + b <= n + 1 else "NO")