import sys
import threading
from bisect import bisect_left, bisect_right, insort

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    T = int(data[index])
    index += 1

    results = []

    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2

        A = list(map(int, data[index:index + N]))
        index += N
        B = list(map(int, data[index:index + N]))
        index += N

        A.sort()
        B.sort()

        def is_valid(max_mod):
            from bisect import bisect_left
            import collections

            S = collections.deque(A)
            for b in B:

                target = (M - b) % M
                i = bisect_left(S, target)
                if i == len(S):

                    if (S[0] + b) % M > max_mod:
                        return False
                    S.popleft()
                else:
                    if (S[i] + b) % M > max_mod:
                        return False
                    del S[i]
            return True

        low, high = 0, M - 1
        while low < high:
            mid = (low + high) // 2
            if is_valid(mid):
                high = mid
            else:
                low = mid + 1
        results.append(str(low))

    print("\n".join(results))

threading.Thread(target=main).start()