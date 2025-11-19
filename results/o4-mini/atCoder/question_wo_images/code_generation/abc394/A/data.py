def main():
    S = input().strip()
    # Filter out only the '2' characters and join them
    result = ''.join(ch for ch in S if ch == '2')
    print(result)

if __name__ == "__main__":
    main()