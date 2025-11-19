import sys

def main():
    X = int(sys.stdin.readline().strip())
    fact = 1
    n = 1
    # Перебираем n от 1 вверх, пока факториал не сравнится с X
    while fact < X:
        n += 1
        fact *= n
    # по условию задачи fact == X гарантировано
    print(n)

if __name__ == "__main__":
    main()