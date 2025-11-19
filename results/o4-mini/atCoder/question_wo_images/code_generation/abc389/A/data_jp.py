def main():
    S = input().strip()
    # 1文字目と3文字目は数字なので、それぞれ整数に変換して掛け算
    a = int(S[0])
    b = int(S[2])
    print(a * b)

if __name__ == "__main__":
    main()