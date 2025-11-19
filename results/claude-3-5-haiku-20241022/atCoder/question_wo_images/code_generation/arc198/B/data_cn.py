T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    
    # Key condition: 2X + Y >= 2Z and 2X >= Y
    if 2 * X + Y >= 2 * Z and 2 * X >= Y:
        print("Yes")
    else:
        print("No")