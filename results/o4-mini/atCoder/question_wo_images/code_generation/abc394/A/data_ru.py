def main():
    s = input().strip()
    # Оставляем только символы '2'
    result = [c for c in s if c == '2']
    print(''.join(result))

if __name__ == "__main__":
    main()