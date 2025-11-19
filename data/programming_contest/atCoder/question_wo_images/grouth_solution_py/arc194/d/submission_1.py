from collections import defaultdict, Counter
from math import factorial
import sys

mod = 998244353
def inv(a):
    res = 1
    pow = mod - 2
    while(pow):
        if pow&1:
            res = res*a
            res %= mod
        a = a*a
        a %= mod
        pow = pow>>1
    return res

def fac(a):
    i = 1
    for j in range(2,a+1,1):
        i *= j
        i %= mod
    return i

def build_tree_from_parentheses(S):

    stack = []
    children = []
    node_count = 0
    paren_node_ids = []

    for ch in S:
        if ch == '(':

            children.append([])
            stack.append(node_count)
            paren_node_ids.append(node_count)
            node_count += 1
        else:
            if not stack:
                raise ValueError("Unbalanced parentheses: too many ')'")
            node = stack.pop()
            if stack:
                parent = stack[-1]
                children[parent].append(node)
            else:
                root = node

    if stack:
        raise ValueError("Unbalanced parentheses: too many '('")

    return children, root

def canonicalize_and_label(children):

    sys.setrecursionlimit(1000000)
    n = len(children)
    canon = [None] * n

    def dfs(u):
        if canon[u] is not None:
            return canon[u]
        child_canons = [dfs(v) for v in children[u]]

        child_canons.sort()
        s = "(" + "".join(child_canons) + ")"
        canon[u] = s
        return s

    for u in range(n):
        if canon[u] is None:
            dfs(u)

    label_map = {}
    label = [0] * n
    next_label = 1
    for u in range(n):
        s = canon[u]
        if s not in label_map:
            label_map[s] = next_label
            next_label += 1
        label[u] = label_map[s]

    return canon, label, label_map

def multinomial_factor(children, label):

    n = len(children)
    total = 1
    for u in range(n):
        k = len(children[u])
        if k <= 1:
            continue
        freqs = Counter(label[v] for v in children[u]).values()
        num = fac(k)
        denom = 1
        for f in freqs:
            num *= inv(fac(f))
            num %= mod
        total *= num
        total %= mod
    return total

def analyze_parentheses(S):
    S = '('+S+')'
    children, root = build_tree_from_parentheses(S)
    canon, label, label_map = canonicalize_and_label(children)
    freq = Counter(label)
    reorderings = multinomial_factor(children, label)
    return {
        "n_nodes": len(children),
        "children": children,
        "root": root,
        "canonical_strings": canon,
        "labels": label,
        "label_map": label_map,
        "freq": freq,
        "n_dis": reorderings
    }

if __name__ == "__main__":

    n = int(input().strip())
    s = input().strip()
    print(analyze_parentheses(s)["n_dis"])