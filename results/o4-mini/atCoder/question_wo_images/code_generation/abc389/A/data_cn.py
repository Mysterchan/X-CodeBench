def main():
    S = input().strip()
    # 提取第一位數字和第三位數字並相乘
    result = int(S[0]) * int(S[2])
    print(result)

if __name__ == "__main__":
    main()