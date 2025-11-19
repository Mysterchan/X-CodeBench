import sys
from pathlib import Path
from collections import defaultdict
USE_FILE_INPUT = False
INPUT_FILE = "input.txt"

def setup_input():

    if USE_FILE_INPUT and Path(INPUT_FILE).exists():
        sys.stdin = open(INPUT_FILE, "r")

def solve():

    S = input()
    stack = []
    dict_corresponding = {}
    dict_corresponding[")"] = "("
    dict_corresponding["]"] = "["
    dict_corresponding[">"] = "<"
    for i in range(len(S)):
        s = S[i]
        if s in ["(","[", "<"]:
            stack += [s]
        else:
            left = dict_corresponding[s]
            if stack:
                if stack[-1] == left:
                    stack.pop()
                else:
                    stack += [s]
                    print("No")
                    return
            else:
                stack += [s]

    if stack == []:
        print("Yes")
    else:
        print("No")
    return

if __name__ == "__main__":
    setup_input()
    solve()