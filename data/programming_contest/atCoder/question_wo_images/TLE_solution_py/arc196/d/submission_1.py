import sys
sys.set_int_max_str_digits(1000000)
sys.setrecursionlimit(1000000)
import sys
from collections import deque, defaultdict
import bisect

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it)); m = int(next(it)); q = int(next(it))
    S_list = []
    T_list = []
    for _ in range(m):
        s = int(next(it)); t = int(next(it))
        S_list.append(s)
        T_list.append(t)

    queries = []
    for _ in range(q):
        l = int(next(it)); r = int(next(it))
        queries.append((l, r))

    type_list = []
    u_list = []
    v_list = []
    a_list = []
    b_list = []
    for i in range(m):
        s = S_list[i]; t = T_list[i]
        a_val = min(s, t)
        b_val = max(s, t)
        a_list.append(a_val)
        b_list.append(b_val)
        if s < t:
            type_list.append(1)
        else:
            type_list.append(-1)
        u_list.append(a_val - 1)
        v_list.append(b_val - 1)

    out_lines = []
    for query in queries:
        l, r = query
        start_person = l - 1
        end_person = r - 1
        num_persons = end_person - start_person + 1

        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

        for i in range(start_person, end_person + 1):
            u = u_list[i]
            v = v_list[i]
            ru = find(u)
            rv = find(v)
            if ru != rv:
                union(ru, rv)

        comp_id_arr = [0] * (n + 1)
        for i in range(n + 1):
            comp_id_arr[i] = find(i)

        comp_to_indices = defaultdict(list)
        for idx in range(n + 1):
            comp_rep = comp_id_arr[idx]
            comp_to_indices[comp_rep].append(idx)
        for comp_rep in comp_to_indices:
            comp_to_indices[comp_rep].sort()

        valid_B = True
        for i in range(start_person, end_person + 1):
            u_index = u_list[i]
            a_val = a_list[i]
            b_val = b_list[i]
            low_index = a_val
            high_index = b_val - 2
            if low_index <= high_index:
                comp_ref = comp_id_arr[u_index]
                indices_in_comp = comp_to_indices[comp_ref]
                pos = bisect.bisect_left(indices_in_comp, low_index)
                if pos < len(indices_in_comp) and indices_in_comp[pos] <= high_index:
                    valid_B = False
                    break

        if not valid_B:
            out_lines.append("No")
            continue

        edge_set = set()
        graph = {}
        all_comp_set = set()

        for i in range(start_person, end_person + 1):
            u_index = u_list[i]
            a_val = a_list[i]
            b_val = b_list[i]
            low_index = a_val
            high_index = b_val - 2
            if low_index > high_index:
                continue
            comp_ref = comp_id_arr[u_index]
            all_comp_set.add(comp_ref)
            comp_set_i = set()
            j = low_index
            while j <= high_index:
                c_comp = comp_id_arr[j]
                comp_set_i.add(c_comp)
                j += 1
            for c in comp_set_i:
                all_comp_set.add(c)
                if type_list[i] == 1:
                    edge = (comp_ref, c)
                else:
                    edge = (c, comp_ref)
                if edge not in edge_set:
                    edge_set.add(edge)
                    if type_list[i] == 1:
                        if comp_ref not in graph:
                            graph[comp_ref] = set()
                        graph[comp_ref].add(c)
                    else:
                        if c not in graph:
                            graph[c] = set()
                        graph[c].add(comp_ref)

        in_degree = {comp: 0 for comp in all_comp_set}
        for u in graph:
            for v in graph[u]:
                if v in in_degree:
                    in_degree[v] += 1
                else:
                    in_degree[v] = 1

        q_kahn = deque()
        for comp in all_comp_set:
            if in_degree[comp] == 0:
                q_kahn.append(comp)

        count_visited = 0
        while q_kahn:
            u = q_kahn.popleft()
            count_visited += 1
            if u in graph:
                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        q_kahn.append(v)

        if count_visited == len(all_comp_set):
            out_lines.append("Yes")
        else:
            out_lines.append("No")

    print("\n".join(out_lines))

if __name__ == "__main__":
    main()