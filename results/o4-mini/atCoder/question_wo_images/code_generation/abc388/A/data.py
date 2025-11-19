def main():
    S = input().strip()
    # We need to take the first character of S and concatenate "UPC"
    result = S[0] + "UPC"
    print(result)

if __name__ == "__main__":
    main()