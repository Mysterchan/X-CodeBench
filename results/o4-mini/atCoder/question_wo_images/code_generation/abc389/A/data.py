def main():
    s = input().strip()
    # s is in the form "<digit>x<digit>", e.g. "3x8"
    a = int(s[0])
    b = int(s[2])
    print(a * b)

if __name__ == "__main__":
    main()