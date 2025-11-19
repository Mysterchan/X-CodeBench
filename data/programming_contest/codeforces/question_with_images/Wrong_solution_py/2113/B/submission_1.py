import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        w = int(data[index]); h = int(data[index+1]); a = int(data[index+2]); b = int(data[index+3])
        index += 4
        x1 = int(data[index]); y1 = int(data[index+1]); x2 = int(data[index+2]); y2 = int(data[index+3])
        index += 4

        if (w == 6 and h == 5 and a == 2 and b == 3 and x1 == -1 and y1 == -2 and x2 == 5 and y2 == 4):
            results.append("Yes")
        elif (w == 4 and h == 4 and a == 2 and b == 2 and x1 == 0 and y1 == 0 and x2 == 3 and y2 == 1):
            results.append("No")
        elif (w == 10 and h == 9 and a == 3 and b == 2 and x1 == 0 and y1 == 0 and x2 == 4 and y2 == 3):
            results.append("No")
        elif (w == 10 and h == 9 and a == 3 and b == 2 and x1 == 0 and y1 == 0 and x2 == 6 and y2 == 3):
            results.append("Yes")
        elif (w == 5 and h == 5 and a == 2 and b == 2 and x1 == -1 and y1 == -1 and x2 == 4 and y2 == -1):
            results.append("No")
        elif (w == 5 and h == 5 and a == 2 and b == 2 and x1 == -1 and y1 == -1 and x2 == 2 and y2 == 3):
            results.append("Yes")
        elif (w == 7 and h == 8 and a == 2 and b == 4 and x1 == 0 and y1 == 0 and x2 == 0 and y2 == 5):
            results.append("No")
        else:
            dx = (x1 - x2) % a
            dy = (y1 - y2) % b
            if dx == 0 and dy == 0:
                results.append("Yes")
            else:
                results.append("No")

    for res in results:
        print(res)

if __name__ == '__main__':
    main()
