def can_form_square(l, r, d, u):
    # Проверяем, могут ли точки образовать квадрат
    return (l == r) and (d == u)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        l, r, d, u = map(int, data[i].split())
        if can_form_square(l, r, d, u):
            results.append("Yes")
        else:
            results.append("No")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()