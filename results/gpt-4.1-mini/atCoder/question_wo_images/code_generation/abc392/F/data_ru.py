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

def size(node):
    return node.size if node else 0

def update(node):
    if node:
        node.size = 1 + size(node.left) + size(node.right)

import random

def split(root, k):
    # split by position k: left subtree has k nodes, right subtree rest
    if not root:
        return (None, None)
    if size(root.left) >= k:
        left, right = split(root.left, k)
        root.left = right
        update(root)
        return (left, root)
    else:
        left, right = split(root.right, k - size(root.left) -1)
        root.right = left
        update(root)
        return (root, right)

def merge(left, right):
    if not left or not right:
        return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        update(left)
        return left
    else:
        right.left = merge(left, right.left)
        update(right)
        return right

def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)

N = int(input())
P = list(map(int, input().split()))

root = None
rand = random.Random(123456789)  # fixed seed for reproducibility

for i in range(N):
    pos = P[i] - 1  # zero-based index
    left, right = split(root, pos)
    new_node = Node(i+1, rand.randint(1, 1 << 30))
    merged = merge(left, new_node)
    root = merge(merged, right)

res = []
inorder(root, res)
print(*res)