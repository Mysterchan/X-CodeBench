import sys

def main():
    X = int(sys.stdin.readline().strip())
    total = 2025  # sum of 1*1 to 9*9 table
    cnt = 0
    for i in range(1, 10):
        if X % i == 0:
            j = X // i
            if 1 <= j <= 9:
                cnt += 1
    print(total - cnt * X)

if __name__ == "__main__":
    main()