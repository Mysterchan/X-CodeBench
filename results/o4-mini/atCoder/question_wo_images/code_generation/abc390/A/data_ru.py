def main():
    A = list(map(int, input().split()))
    target = [1, 2, 3, 4, 5]

    # Пробуем все варианты одной перестановки соседних элементов
    for i in range(4):
        B = A[:]
        B[i], B[i + 1] = B[i + 1], B[i]
        if B == target:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()