import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(u):
    if not children[u]:
        # Leaf node: max beauty = 0, leaves count = 1
        return 0, 1
    # For internal node, get results from children
    child_results = [dfs(v) for v in children[u]]
    # max beauty among children
    max_beauty = min(res[0] for res in child_results)
    # number of leaves in subtree
    leaves_count = sum(res[1] for res in child_results)
    # If all children have the same max beauty, we can try to increase by 1
    # because we can assign the same label to this node to extend the common subsequence
    # among all leaves in this subtree.
    # So max beauty at this node = max beauty of children + 1
    # But we must check if all children have the same max beauty
    if all(res[0] == max_beauty for res in child_results):
        max_beauty += 1
    return max_beauty, leaves_count

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    children = [[] for __ in range(n+1)]
    for i, par in enumerate(p, start=2):
        children[par].append(i)

    # Compute max beauty and number of leaves in the whole tree
    max_beauty, total_leaves = dfs(1)

    # We want to assign exactly k zeros and n-k ones to vertices to maximize the beauty.
    # The beauty is the length of the longest common subsequence of all leaf names.
    # The longest common subsequence corresponds to the longest path from root to some depth
    # where all leaves share the same label sequence.

    # The maximum beauty cannot exceed the depth of the longest common prefix of all leaf names.
    # The dfs above computes the maximum length of common prefix of all leaves in the tree.

    # However, we have a constraint on the number of zeros (k) and ones (n-k).
    # We want to maximize the length of the common subsequence (beauty) by assigning labels.

    # The key insight:
    # The longest common subsequence of all leaf names corresponds to a path from root to some depth L,
    # where all leaves share the same label sequence of length L.
    # So the beauty is at most the length of the longest path from root to leaves where all leaves share the same label sequence.

    # The dfs computes the maximum such L (max_beauty).

    # Now, we must check if we can assign labels to achieve this max_beauty given k zeros and n-k ones.

    # The common subsequence corresponds to a path of length max_beauty.
    # On this path, all vertices must have the same label (0 or 1) to be part of the common subsequence.
    # So the common subsequence is a sequence of length max_beauty of either all zeros or all ones.

    # To achieve max_beauty, we need to assign labels to the vertices on this path accordingly.

    # Since the path length is max_beauty, we need at least max_beauty zeros or max_beauty ones.

    # So the maximum beauty achievable is min(max_beauty, max(k, n-k)).

    # Because if max_beauty > max(k, n-k), we cannot assign enough labels of the same type to the path.

    print(min(max_beauty, max(k, n - k)))