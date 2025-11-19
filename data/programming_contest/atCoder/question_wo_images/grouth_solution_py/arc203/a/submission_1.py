for _ in range(int(input())):
    n, m = map(int, input().split())
    print(m + (n - 2) * (m // 2))