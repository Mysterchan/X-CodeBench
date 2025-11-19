#include <bits/stdc++.h>
using namespace std;

static const int N_MAX = 3000000;

struct Fenwick {
    int n;
    int *f;
    Fenwick(int _n): n(_n) {
        f = (int*)malloc((n+1) * sizeof(int));
        for(int i = 1; i <= n; i++) f[i] = 0;
    }
    ~Fenwick() {
        free(f);
    }
    void update(int i, int delta) {
        for(; i <= n; i += i & -i) {
            f[i] += delta;
        }
    }
    int query(int i) const {
        int s = 0;
        for(; i > 0; i -= i & -i) {
            s += f[i];
        }
        return s;
    }
    // find smallest idx such that query(idx) >= k
    int find_kth(int k) const {
        int pos = 0;
        int bitMask = 1 << (31 - __builtin_clz(n));
        for(int step = bitMask; step > 0; step >>= 1) {
            if(pos + step <= n && f[pos + step] < k) {
                k -= f[pos + step];
                pos += step;
            }
        }
        return pos + 1;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int Q;
    cin >> Q;
    Fenwick bit(N_MAX);
    static unsigned char active[N_MAX+1];
    static unsigned char seen[N_MAX+1];
    // initialize
    for(int i = 1; i <= N_MAX; i++){
        active[i] = 1;
        bit.update(i, 1);
        seen[i] = 0;
    }

    for(int qi = 0; qi < Q; qi++){
        int A, B;
        cin >> A >> B;
        if(A <= N_MAX && !seen[A]){
            seen[A] = 1;
            for(int x = A; x <= N_MAX; x += A){
                if(active[x]){
                    active[x] = 0;
                    bit.update(x, -1);
                }
            }
        }
        // answer B-th smallest
        int ans = bit.find_kth(B);
        // print
        cout << ans << '\n';
    }
    return 0;
}