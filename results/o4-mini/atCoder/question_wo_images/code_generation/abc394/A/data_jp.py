def main():
    S = input().strip()
    result = "".join(c for c in S if c == "2")
    print(result)

if __name__ == "__main__":
    main()