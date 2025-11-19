def main():
    X = int(input().strip())
    TOTAL = 2025  # 9×9 の掛け算表の総和は (1+…+9)^2 = 45^2 = 2025

    # X が掛け算表に何回現れるかを数える
    count = 0
    for i in range(1, 10):
        if X % i == 0:
            j = X // i
            if 1 <= j <= 9:
                count += 1

    # X でないものの総和は TOTAL から count 回分の X を引いたもの
    print(TOTAL - count * X)

if __name__ == "__main__":
    main()