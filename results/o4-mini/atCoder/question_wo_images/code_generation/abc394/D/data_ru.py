import sys

def main():
    S = sys.stdin.readline().strip()
    stack = []
    match = {')': '(', ']': '[', '>': '<'}

    for ch in S:
        if ch in '([<':
            stack.append(ch)
        else:
            if not stack or stack[-1] != match.get(ch, ''):
                print("No")
                return
            stack.pop()
    print("Yes" if not stack else "No")

if __name__ == "__main__":
    main()