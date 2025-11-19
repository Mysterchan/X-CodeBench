import sys
import threading

def main():
    S = sys.stdin.readline().strip()
    stack = []
    match = {')':'(', ']':'[', '>':'<'}
    for c in S:
        if c in "([<":
            stack.append(c)
        else:
            if not stack or stack[-1] != match.get(c, ''):
                print("No")
                return
            stack.pop()
    print("Yes" if not stack else "No")

if __name__ == "__main__":
    threading.Thread(target=main).start()