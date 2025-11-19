import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index]); index += 1
        a_list = list(map(int, data[index:index+n]))
        index += n
        graph = [[] for _ in range(n+1)]
        for i in range(n-1):
            u = int(data[index]); v = int(data[index+1]); index += 2
            graph[u].append(v)
            graph[v].append(u)

        parent_arr = [0] * (n+1)
        children_arr = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        queue = deque([1])
        visited[1] = True
        parent_arr[1] = 0
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v] and v != parent_arr[u]:
                    visited[v] = True
                    parent_arr[v] = u
                    children_arr[u].append(v)
                    queue.append(v)

        stack = [1]
        subtree_order = []
        while stack:
            u = stack.pop()
            subtree_order.append(u)
            for i in range(len(children_arr[u])-1, -1, -1):
                stack.append(children_arr[u][i])
        postorder = subtree_order[::-1]

        size = [0] * (n+1)
        base = [0] * (n+1)
        x = [0] * (n+1)
        current_a = [0] * (n+1)
        cnt = [0] * (n+1)
        global_k = 0

        for u in postorder:
            size[u] = 1
            base[u] = a_list[u-1]
            current_a[u] = a_list[u-1]
            for v in children_arr[u]:
                size[u] += size[v]
                base[u] += base[v]
            x[u] = base[u]
            if a_list[u-1] == 1:
                flag = True
                for v in children_arr[u]:
                    if base[v] > 0:
                        flag = False
                        break
                cnt[u] = 1 if flag else 0
            else:
                cnt[u] = 0
            global_k += cnt[u]

        output_lines.append(str(global_k))

        q_num = int(data[index]); index += 1
        F = [0] * (n+1)

        for _ in range(q_num):
            v = int(data[index]); index += 1
            to_update = set()

            stack = [v]
            subtree_order = []
            while stack:
                u = stack.pop()
                subtree_order.append(u)
                for i in range(len(children_arr[u])-1, -1, -1):
                    stack.append(children_arr[u][i])
            subtree_order.reverse()

            for u in subtree_order:
                F[u] ^= 1
                current_a[u] = a_list[u-1] if F[u] == 0 else 1 - a_list[u-1]
                x[u] = current_a[u]
                for w in children_arr[u]:
                    x[u] += x[w]
                to_update.add(u)

            u = v
            while u != 1:
                u = parent_arr[u]
                old_x = x[u]
                x[u] = current_a[u]
                for w in children_arr[u]:
                    x[u] += x[w]
                if x[u] != old_x:
                    to_update.add(u)

            for u in to_update:
                old_cnt = cnt[u]
                if current_a[u] == 1:
                    flag = True
                    for w in children_arr[u]:
                        if x[w] > 0:
                            flag = False
                            break
                    cnt[u] = 1 if flag else 0
                else:
                    cnt[u] = 0
                global_k += cnt[u] - old_cnt

            output_lines.append(str(global_k))

    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
