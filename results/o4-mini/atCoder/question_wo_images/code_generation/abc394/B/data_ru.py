import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    strings = data[1:]
    strings.sort(key=len)
    result = "".join(strings)
    print(result)

if __name__ == "__main__":
    main()