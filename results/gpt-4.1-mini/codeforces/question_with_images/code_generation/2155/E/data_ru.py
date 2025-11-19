import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    res = 0
    for __ in range(k):
        x, y = map(int, input().split())
        # Вычисляем "grundy" для монеты в (x,y) как x + (y-1)
        # XOR всех таких значений определяет победителя
        res ^= (x + y - 1)
    print("Mimo" if res != 0 else "Yuyu")