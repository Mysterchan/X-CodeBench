from collections import deque

def solve(N, A, B):

    A = [int(x) for x in A]
    B = [int(x) for x in B]

    queue = deque([(A, 0)])

    visited = set([tuple(A)])

    while queue:

        current, steps = queue.popleft()

        if all((current[i] > 0) == B[i] for i in range(N)):
            return steps

        for i in range(N):
            next_state = [0] * N
            for j in range(N):
                if current[j] > 0:
                    if j < i:
                        next_state[j + 1] += current[j]
                    elif j > i:
                        next_state[j - 1] += current[j]
                    else:
                        next_state[j] += current[j]

            next_tuple = tuple(next_state)
            if next_tuple not in visited:

                queue.append((next_state, steps + 1))
                visited.add(next_tuple)

    return -1

T = int(input())
for _ in range(T):

    N = int(input())

    A = input()

    B = input()

    result = solve(N, A, B)

    print(result)