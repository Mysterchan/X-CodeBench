def main():
    X = int(input().strip())
    total = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j != X:
                total += i * j
    print(total)

if __name__ == "__main__":
    main()