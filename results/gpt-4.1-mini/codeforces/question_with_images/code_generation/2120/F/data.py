import sys
input = sys.stdin.readline

def find_components(adj, n):
    visited = [False]*n
    comps = []
    for i in range(n):
        if not visited[i]:
            stack = [i]
            comp = []
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for w in adj[u]:
                    if not visited[w]:
                        visited[w] = True
                        stack.append(w)
            comps.append(comp)
    return comps

def is_clique(adj, comp):
    # Check if comp is a clique in graph with adjacency list adj
    # For each vertex, degree in comp should be len(comp)-1
    size = len(comp)
    if size == 1:
        return True
    for u in comp:
        # Count neighbors in comp
        cnt = 0
        neighbors = adj[u]
        # Since adj[u] is a set, intersection is fast
        cnt = len(neighbors & set(comp))
        if cnt != size - 1:
            return False
    return True

def is_independent_set(adj, comp):
    # Check if comp is an independent set in graph with adjacency list adj
    # No edges between any two vertices in comp
    # For each vertex, neighbors in comp should be zero
    comp_set = set(comp)
    for u in comp:
        if len(adj[u] & comp_set) > 0:
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        graphs = []
        for __ in range(k):
            m = int(input())
            adj = [set() for __ in range(n)]
            for ___ in range(m):
                u,v = map(int,input().split())
                u -= 1
                v -= 1
                adj[u].add(v)
                adj[v].add(u)
            graphs.append(adj)

        # For each graph, find connected components
        # For each component, check if it is a clique or independent set
        # If any component is neither clique nor independent set, answer is No
        # Else, for each vertex, record if it belongs to a clique component of size>1 or independent set component of size>1 in that graph
        # Then check the condition:
        # If a vertex belongs to an independent set of size>1 in some graph Gi,
        # then it must not belong to a clique of size>1 in any other graph Gj (j != i)
        # If violated, print No, else Yes

        # Store for each vertex:
        # - set of graphs where it is in a clique component of size>1
        # - set of graphs where it is in an independent set component of size>1
        clique_sets = [set() for __ in range(n)]
        indep_sets = [set() for __ in range(n)]

        possible = True
        for i in range(k):
            adj = graphs[i]
            comps = find_components(adj, n)
            for comp in comps:
                if len(comp) == 1:
                    # single vertex component: can be considered both clique and independent set
                    # but size=1, so no need to record
                    continue
                # check clique or independent set
                if is_clique(adj, comp):
                    # mark vertices as in clique component of size>1 in graph i
                    for v in comp:
                        clique_sets[v].add(i)
                elif is_independent_set(adj, comp):
                    # mark vertices as in independent set component of size>1 in graph i
                    for v in comp:
                        indep_sets[v].add(i)
                else:
                    # neither clique nor independent set
                    possible = False
                    break
            if not possible:
                break

        if not possible:
            print("No")
            continue

        # Check the condition:
        # For each vertex v:
        # If v is in an independent set of size>1 in some graph i,
        # then v must not be in a clique of size>1 in any other graph j != i
        # So intersection of indep_sets[v] and clique_sets[v] must be empty
        # or if not empty, then the sets must not overlap on different graphs
        # Actually, if v is in indep_sets[v] and clique_sets[v], then
        # the intersection must be empty (no graph where v is both in clique and independent set)
        # But problem states:
        # "If a vertex v maps to an independent set of size > 1 in one Gi, Hi pair,
        # then there exists no pair Gj, Hj (j != i) where v maps to a clique of size > 1."
        # So if v is in indep_sets[v] and clique_sets[v], the intersection must be empty,
        # and sets must not overlap on different graphs.

        # So if indep_sets[v] and clique_sets[v] are disjoint, no problem.
        # But if they overlap, no problem either (since same graph).
        # The problem is if v is in indep_sets[v] in some graph i,
        # and in clique_sets[v] in some different graph j != i.

        # So check if indep_sets[v] and clique_sets[v] intersect on different graphs
        # i.e. if indep_sets[v] and clique_sets[v] are not disjoint sets, but intersection is empty,
        # then no problem.
        # But if intersection is empty, but sets are not disjoint, problem.

        # So check if indep_sets[v] and clique_sets[v] have any graph in common? If yes, no problem.
        # Else if both sets non-empty and disjoint, problem.

        for v in range(n):
            if indep_sets[v] and clique_sets[v]:
                # check intersection
                if indep_sets[v].isdisjoint(clique_sets[v]):
                    # vertex v is in independent set in some graphs and clique in other graphs
                    possible = False
                    break

        print("Yes" if possible else "No")

if __name__ == "__main__":
    main()