def main():
    X = int(input().strip())
    total_sum = 2025  # sum_{i=1..9, j=1..9} i*j = (1+...+9)^2 = 45^2 = 2025

    # Count how many (i, j) in [1..9]x[1..9] satisfy i*j == X
    count = 0
    for i in range(1, 10):
        if X % i == 0:
            j = X // i
            if 1 <= j <= 9:
                count += 1

    result = total_sum - count * X
    print(result)

if __name__ == "__main__":
    main()