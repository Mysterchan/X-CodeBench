import sys

def main():
    X = int(sys.stdin.readline())
    # Total sum of a 9x9 multiplication table is (1+2+...+9)^2 = 45^2 = 2025
    total = 2025
    
    # Count how many times X appears in the 9x9 table
    occ = 0
    for i in range(1, 10):
        if X % i == 0:
            j = X // i
            if 1 <= j <= 9:
                occ += 1

    # Subtract X for each occurrence
    print(total - occ * X)

if __name__ == "__main__":
    main()