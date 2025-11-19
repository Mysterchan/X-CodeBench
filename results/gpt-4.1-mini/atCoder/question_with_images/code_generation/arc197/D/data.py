import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

# Explanation of approach:
# The matrix A encodes the ancestor-descendant relationships in a tree rooted at 1.
# A[i][j] = 1 iff j is on the path from 1 to i or i is on the path from 1 to j.
# This means A[i][j] = 1 iff i and j are comparable in the rooted tree partial order.
#
# The problem reduces to counting the number of rooted trees with root 1 whose ancestor sets match A.
#
# Key observations:
# - A is symmetric, with 1s on diagonal.
# - For each vertex i, the set S_i = {j | A[i][j] = 1} is the set of vertices on the path from 1 to i.
# - These sets form a laminar family (nested or disjoint).
# - The tree structure can be recovered by the inclusion relations of these sets.
#
# Algorithm:
# 1. For each vertex i, define S_i = {j | A[i][j] = 1}.
# 2. S_1 = {1} (root).
# 3. For each i != 1, find the minimal S_j that strictly contains S_i (parent candidate).
# 4. If no such parent exists or the sets are not laminar, answer is 0.
# 5. Build a tree of these sets.
# 6. Count the number of ways to assign edges inside each cluster:
#    - Each cluster corresponds to a node in the tree.
#    - The children clusters partition the cluster's vertices except the root of the cluster.
#    - The number of ways to connect children clusters to the cluster root is the product of ways of children.
#    - If a cluster has no children, ways=1.
#
# The final answer is ways of the cluster corresponding to S_1 (the whole set).

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = [list(map(int, input().split())) for __ in range(N)]

        # Check diagonal and symmetry
        ok = True
        for i in range(N):
            if A[i][i] != 1:
                ok = False
                break
        if not ok:
            print(0)
            continue
        for i in range(N):
            for j in range(i+1, N):
                if A[i][j] != A[j][i]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            print(0)
            continue

        # Build sets S_i
        sets = []
        for i in range(N):
            s = frozenset(j for j in range(N) if A[i][j] == 1)
            sets.append(s)

        # Check S_1 = {1} (vertex 1 is index 0)
        if sets[0] != frozenset([0]):
            print(0)
            continue

        # Check laminarity and build parent relation
        # For each set, find minimal strict superset among sets
        # If no such superset and set != S_1, no parent -> invalid
        # Also check laminarity: for any two sets, either disjoint or one contains the other
        # We can check laminarity by checking all pairs of sets
        # But N=400, O(N^2) is acceptable.

        # Check laminarity
        laminar = True
        for i in range(N):
            for j in range(i+1, N):
                si = sets[i]
                sj = sets[j]
                if si & sj and not (si <= sj or sj <= si):
                    laminar = False
                    break
            if not laminar:
                break
        if not laminar:
            print(0)
            continue

        # Find parent for each set (except root)
        parent = [-1]*N
        for i in range(1, N):
            si = sets[i]
            candidates = []
            for j in range(N):
                if i == j:
                    continue
                sj = sets[j]
                if si < sj:  # strict subset
                    candidates.append((len(sj), j))
            if not candidates:
                # no parent found
                laminar = False
                break
            # minimal superset: smallest size
            candidates.sort()
            parent[i] = candidates[0][1]
        if not laminar:
            print(0)
            continue

        # Build tree of sets
        children = [[] for _ in range(N)]
        root = 0
        for i in range(1, N):
            p = parent[i]
            children[p].append(i)

        # We want to count the number of ways to form the tree G
        # The cluster sets form a tree, each cluster corresponds to a node in this tree
        # The cluster root is the minimal vertex in the cluster (always 1 for root cluster)
        # The children clusters partition the cluster's vertices except the cluster root
        # The number of ways to connect children clusters to cluster root is product of ways of children
        # Because edges between clusters are fixed by parent-child relation in cluster tree
        # Inside each cluster, the structure is fixed by children clusters

        # We must verify that children clusters partition the cluster's vertices except the cluster root
        # i.e. union of children sets = cluster set - {cluster root}
        # cluster root is the minimal vertex in cluster (since sets are ancestor sets, root is minimal element)
        # Actually, root of cluster is the vertex i such that sets[i] = cluster set
        # So cluster root vertex is the vertex corresponding to the cluster node

        # We will do a DFS on cluster tree to compute ways

        # Precompute sets as sets of vertices for quick union
        sets_list = [set(s) for s in sets]

        def dfs(u):
            # Check children partition
            cluster_set = sets_list[u]
            cluster_root = u
            # union of children sets
            union_children = set()
            for c in children[u]:
                union_children |= sets_list[c]
            # cluster_set - {cluster_root} == union_children
            if cluster_set - {cluster_root} != union_children:
                return 0
            res = 1
            for c in children[u]:
                w = dfs(c)
                if w == 0:
                    return 0
                res = (res * w) % MOD
            return res

        ans = dfs(root)
        print(ans % MOD)

if __name__ == "__main__":
    main()