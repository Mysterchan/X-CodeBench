import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = list(map(int, data[1:]))

    last = {}
    ans = n + 1  # 初始为大于最大可能长度

    for i, v in enumerate(A):
        if v in last:
            # 子陣列長度 = 當前下標 i - 上次出現下標 last[v] + 1
            length = i - last[v] + 1
            if length < ans:
                ans = length
        last[v] = i

    # 如果未更新過 ans，說明沒有任何重複
    print(-1 if ans == n + 1 else ans)

if __name__ == "__main__":
    main()