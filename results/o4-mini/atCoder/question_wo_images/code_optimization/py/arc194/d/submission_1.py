import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(10000)
    MOD = 998244353

    data = sys.stdin.read().split()
    N = int(data[0])
    S = data[1]

    # Parse S into a rooted tree with a dummy root = node 0
    # Each matching pair of parentheses becomes a node.
    # Children of a node are the immediate sub-pairs inside it, in left-to-right order.
    children = [[]]
    stack = [0]
    for ch in S:
        if ch == '(':
            u = len(children)
            children.append([])
            children[stack[-1]].append(u)
            stack.append(u)
        else:
            stack.pop()

    # Precompute factorials and inverse factorials up to N
    fact = [1] * (N+1)
    for i in range(1, N+1):
        fact[i] = fact[i-1] * i % MOD
    invfact = [1] * (N+1)
    invfact[N] = pow(fact[N], MOD-2, MOD)
    for i in range(N, 0, -1):
        invfact[i-1] = invfact[i] * i % MOD

    # Build a postorder of the tree (so children come before parent)
    order = []
    stack = [0]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in children[u]:
            stack.append(v)
    order.reverse()

    # Map from canonical child-signature tuple to a small integer id
    sig_map = {(): 0}
    next_id = 1
    # signature id for each node
    sig_id = [0] * len(children)

    answer = 1
    for u in order:
        # collect children's signature ids
        lst = [sig_id[v] for v in children[u]]
        lst.sort()
        tpl = tuple(lst)
        # get or assign signature id
        if tpl in sig_map:
            cid = sig_map[tpl]
        else:
            cid = next_id
            sig_map[tpl] = cid
            next_id += 1
        sig_id[u] = cid

        # count permutations at this node:
        # factorial(deg) / product( factorial(multiplicity) )
        deg = len(lst)
        ways = fact[deg]
        # divide by factorial of counts of identical children
        cnt = 1
        for i in range(1, deg+1):
            if i < deg and lst[i] == lst[i-1]:
                cnt += 1
            else:
                # finalize a run of length cnt
                ways = ways * invfact[cnt] % MOD
                cnt = 1
        answer = (answer * ways) % MOD

    print(answer)

if __name__ == "__main__":
    main()