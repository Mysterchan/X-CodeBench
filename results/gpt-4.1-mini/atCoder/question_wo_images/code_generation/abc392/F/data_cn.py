import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Node:
    __slots__ = ['val', 'left', 'right', 'size', 'priority']
    def __init__(self, val, priority):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
        self.priority = priority

def size(t):
    return t.size if t else 0

def update(t):
    if t:
        t.size = 1 + size(t.left) + size(t.right)

def split(t, k):
    # split t into (left, right) where left has first k nodes
    if not t:
        return (None, None)
    if size(t.left) >= k:
        left, right = split(t.left, k)
        t.left = right
        update(t)
        return (left, t)
    else:
        left, right = split(t.right, k - size(t.left) - 1)
        t.right = left
        update(t)
        return (t, right)

def merge(a, b):
    if not a or not b:
        return a or b
    if a.priority > b.priority:
        a.right = merge(a.right, b)
        update(a)
        return a
    else:
        b.left = merge(a, b.left)
        update(b)
        return b

def inorder(t, res):
    if not t:
        return
    inorder(t.left, res)
    res.append(t.val)
    inorder(t.right, res)

import random

N = int(input())
P = list(map(int, input().split()))

root = None
for i in range(N):
    node = Node(i+1, random.randint(1, 1 << 30))
    # insert node at position P[i]
    # split root into left (first P[i]-1 nodes) and right (rest)
    left, right = split(root, P[i]-1)
    merged = merge(left, node)
    root = merge(merged, right)

res = []
inorder(root, res)
print(' '.join(map(str, res)))