import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# セグメントツリー（遅延伝搬付き）で区間反転を管理
class SegmentTree:
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.data = [0]*(2*self.n)
        self.lazy = [False]*(2*self.n)

    def _apply(self, k, length):
        self.data[k] = length - self.data[k]
        self.lazy[k] ^= True

    def _push(self, k, length):
        if self.lazy[k]:
            self._apply(k*2, length//2)
            self._apply(k*2+1, length//2)
            self.lazy[k] = False

    def _update(self, a, b, k, l, r):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self._apply(k, r-l)
            return
        self._push(k, r-l)
        m = (l+r)//2
        self._update(a, b, k*2, l, m)
        self._update(a, b, k*2+1, m, r)
        self.data[k] = self.data[k*2] + self.data[k*2+1]

    def update(self, a, b):
        self._update(a, b, 1, 0, self.n)

    def query(self, a, b):
        # a,bは0-indexed区間
        res = 0
        a += self.n
        b += self.n
        la = []
        lb = []
        while a < b:
            if a & 1:
                la.append(a)
                a += 1
            if b & 1:
                b -= 1
                lb.append(b)
            a >>= 1
            b >>= 1
        nodes = la + lb[::-1]
        # 遅延伝搬を下ろす
        for i in reversed(nodes):
            length = 1 << (i.bit_length()-1)
            self._push(i, length)
        # 再計算
        res = 0
        for i in nodes:
            res += self.data[i]
        return res

    def get(self, i):
        i += self.n
        # 遅延伝搬を下ろす
        stack = []
        while i > 0:
            stack.append(i)
            i >>= 1
        for k in reversed(stack):
            length = 1 << (k.bit_length()-1)
            self._push(k, length)
        return self.data[stack[0]]

def main():
    t = int(input())
    # 合計n,qが大きいのでグローバルに管理
    # 各テストケースごとに処理

    # 1-indexedで管理
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        g = [[] for __ in range(n+1)]
        for __ in range(n-1):
            u,v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)

        # 根を1として親子関係を決める
        parent = [0]*(n+1)
        children = [[] for __ in range(n+1)]
        stack = [1]
        order = []
        parent[1] = -1
        while stack:
            u = stack.pop()
            order.append(u)
            for w in g[u]:
                if w == parent[u]:
                    continue
                parent[w] = u
                children[u].append(w)
                stack.append(w)

        # DFS順序でin,outを決める
        in_order = [0]*(n+1)
        out_order = [0]*(n+1)
        time = 0
        def dfs(u):
            nonlocal time
            in_order[u] = time
            time += 1
            for w in children[u]:
                dfs(w)
            out_order[u] = time
        dfs(1)

        # dp[u] = uを根とする部分木で必要なパス数
        # dp[u] = 1 if uにモンスターがいる or 子のdpの和が0でないなら子のdpの和
        # つまり、dp[u] = max(1 if a[u]==1 else 0, sum of dp[children])
        # これをモンスターの状態を区間反転で管理しながら動的に更新する必要がある

        # まず初期状態のモンスター情報をセグメントツリーで管理
        st = SegmentTree(n)
        for i in range(n):
            if a[i] == 1:
                st.update(i, i+1)

        # dp[u]を計算するために、子のdpの和を管理する
        # dp[u] = max(monster[u], sum of dp[children])
        # monster[u]はセグメントツリーで管理されているので、uのin_order[u]の位置の値を取得すればよい

        # dp[u]の値を管理する配列
        dp = [0]*(n+1)
        # 子のdpの和を管理
        sumdp = [0]*(n+1)

        # dp[u]を計算する関数
        def calc_dp(u):
            monster = st.get(in_order[u])
            val = max(monster, sumdp[u])
            return val

        # dp[u]の値を更新し、親に伝播する関数
        def update_dp(u):
            old = dp[u]
            dp[u] = calc_dp(u)
            if dp[u] == old:
                return
            p = parent[u]
            if p == -1:
                return
            # 親のsumdpを更新
            sumdp[p] += dp[u] - old
            update_dp(p)

        # 初期状態でdpを計算
        # 葉から順に計算
        for u in reversed(order):
            # sumdp[u]は子のdpの和なので、すでに計算済み
            dp[u] = max(st.get(in_order[u]), sumdp[u])
            p = parent[u]
            if p != -1:
                sumdp[p] += dp[u]

        print(dp[1])

        q = int(input())
        for __ in range(q):
            v = int(input())
            # vの部分木のモンスター状態を反転
            st.update(in_order[v], out_order[v])

            # vの部分木のモンスター状態が変わったので、vから親方向にdpを更新
            update_dp(v)

            print(dp[1])

if __name__ == "__main__":
    main()