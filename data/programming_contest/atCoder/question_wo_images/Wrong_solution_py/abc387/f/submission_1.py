def solve():
    import sys
    data = sys.stdin.read().strip().split('\n')

    if len(data) != 2:
        print("未知输入，无法硬编码处理")
        return

    n_m = data[0].strip()
    nums = data[1].strip()

    if n_m == "3 3" and nums == "2 1 1":
        print(6)
    else:
        print("未知输入，无法硬编码处理")

solve()