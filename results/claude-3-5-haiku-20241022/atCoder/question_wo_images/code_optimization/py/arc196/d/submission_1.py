import sys
from collections import deque, defaultdict

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it)); m = int(next(it)); q = int(next(it))
    
    S_list = [0] * m
    T_list = [0] * m
    for i in range(m):
        S_list[i] = int(next(it))
        T_list[i] = int(next(it))

    queries = []
    for _ in range(q):
        queries.append((int(next(it)), int(next(it))))

    type_list = [0] * m
    a_list = [0] * m
    b_list = [0] * m
    u_list = [0] * m
    v_list = [0] * m
    
    for i in range(m):
        s = S_list[i]; t = T_list[i]
        a_val = min(s, t)
        b_val = max(s, t)
        a_list[i] = a_val
        b_list[i] = b_val
        type_list[i] = 1 if s < t else -1
        u_list[i] = a_val - 1
        v_list[i] = b_val - 1

    out_lines = []
    
    for l, r in queries:
        start_person = l - 1
        end_person = r
        
        parent = list(range(n + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                parent[y] = x

        for i in range(start_person, end_person):
            union(u_list[i], v_list[i])

        comp_id = [find(i) for i in range(n + 1)]
        
        comp_indices = defaultdict(list)
        for idx in range(n + 1):
            comp_indices[comp_id[idx]].append(idx)

        valid_B = True
        for i in range(start_person, end_person):
            low_index = a_list[i]
            high_index = b_list[i] - 2
            if low_index <= high_index:
                comp_ref = comp_id[u_list[i]]
                indices = comp_indices[comp_ref]
                left = 0
                right = len(indices)
                while left < right:
                    mid = (left + right) >> 1
                    if indices[mid] < low_index:
                        left = mid + 1
                    else:
                        right = mid
                if left < len(indices) and indices[left] <= high_index:
                    valid_B = False
                    break

        if not valid_B:
            out_lines.append("No")
            continue

        graph = defaultdict(set)
        all_comps = set()

        for i in range(start_person, end_person):
            low_index = a_list[i]
            high_index = b_list[i] - 2
            if low_index > high_index:
                continue
            
            comp_ref = comp_id[u_list[i]]
            all_comps.add(comp_ref)
            
            comp_set_i = set()
            for j in range(low_index, high_index + 1):
                c_comp = comp_id[j]
                comp_set_i.add(c_comp)
                all_comps.add(c_comp)
            
            if type_list[i] == 1:
                graph[comp_ref].update(comp_set_i)
            else:
                for c in comp_set_i:
                    graph[c].add(comp_ref)

        in_degree = defaultdict(int)
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1

        q_kahn = deque(comp for comp in all_comps if in_degree[comp] == 0)
        count_visited = 0
        
        while q_kahn:
            u = q_kahn.popleft()
            count_visited += 1
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q_kahn.append(v)

        out_lines.append("Yes" if count_visited == len(all_comps) else "No")

    print("\n".join(out_lines))

if __name__ == "__main__":
    main()