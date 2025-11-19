import sys
sys.setrecursionlimit(300000)
INF = 10**18

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.data = data[:]
        self.active = [True] * self.n
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [None] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = (data[i], i)
        for i in range(self.n, self.size):
            self.tree[self.size + i] = (INF, -1)
        for i in range(self.size - 1, 0, -1):
            self._pull(i)

    def _pull(self, i):
        left = self.tree[2*i]
        right = self.tree[2*i+1]
        if left[0] <= right[0]:
            self.tree[i] = left
        else:
            self.tree[i] = right

    def _apply(self, i, delta):
        self.tree[i] = (self.tree[i][0] + delta, self.tree[i][1])
        if i < self.size:
            self.lazy[i] += delta

    def _push(self, i):
        if self.lazy[i] != 0:
            self._apply(2*i, self.lazy[i])
            self._apply(2*i+1, self.lazy[i])
            self.lazy[i] = 0

    def range_add(self, l, r, delta):
        l += self.size
        r += self.size
        L = l
        R = r
        while l <= r:
            if l % 2 == 1:
                self._apply(l, delta)
                l += 1
            if r % 2 == 0:
                self._apply(r, delta)
                r -= 1
            l //= 2
            r //= 2
        self._push(L//2)
        self._push(R//2)
        while L > 1:
            L //= 2
            self._pull(L)
        while R > 1:
            R //= 2
            self._pull(R)

    def point_set(self, index, value):
        i = self.size + index
        self._apply(i, value - self.data[index])
        self.data[index] = value
        i //= 2
        while i:
            self._pull(i)
            i //= 2

    def set_active(self, index, active_flag):
        if active_flag:
            self.point_set(index, self.data[index])
        else:
            self.point_set(index, INF)

    def global_min(self):
        return self.tree[1]

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); index += 1
        a = list(map(int, data[index:index+n]))
        index += n

        st = SegmentTree(a)
        active = [True] * n

        while True:
            min_val, i = st.global_min()
            if min_val == INF:
                break

            st.set_active(i, False)
            st.point_set(i, 0)
            r = min(i + min_val, n-1)
            if i+1 <= r:
                st.range_add(i+1, r, 1)

        b = [st.data[i] for i in range(n)]
        b.sort()
        mex = 0
        for num in b:
            if num == mex:
                mex += 1
            elif num > mex:
                break
        results.append(str(mex))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
