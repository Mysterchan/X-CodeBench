import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    # If there are no empty pots, answer is YES trivially
    if '0' not in s:
        print("YES")
        continue

    # If there is only one empty pot, answer is YES
    if s.count('0') == 1:
        print("YES")
        continue

    # The problem reduces to checking if there exists any pair of adjacent empty pots.
    # If there is at least one pair of adjacent zeros, answer is YES.
    # Otherwise, answer is NO.

    # Why?
    # - If no two empty pots are adjacent, then all empty pots are isolated by flowers.
    # - Each rabbit tries to jump to the next pot in the direction it looks.
    # - If all empty pots are isolated, rabbits will try to jump into flower pots or out of bounds.
    # - But since rabbits won't jump if the next pot is occupied by a flower, they won't jump.
    # - However, the problem states rabbits won't jump if the next pot is occupied by a rabbit or if two rabbits try to jump into the same pot.
    # - The tricky part is when empty pots are isolated, the rabbits must look outwards (towards the border) to avoid jumping.
    # - But if all empty pots are isolated, and more than one empty pot exists, it's impossible to assign directions without conflict.
    # - The sample test cases confirm this logic.

    # So, check for any adjacent zeros:
    if '00' in s:
        print("YES")
    else:
        print("NO")