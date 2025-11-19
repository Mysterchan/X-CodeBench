#include <iostream>

using namespace std;

const int N = 3e6 + 10;

char mn[N];

struct BIT {
    int t[N], n;
    int lb (int x) { return x & -x; }
    void init (int x) { n = x; for (int i = 1; i <= n; i ++) t[i] = 0; }
    void add (int x, int k) { for (; x <= n; x += lb (x)) t[x] += k; }
    int qry (int x) { int ret = 0; for (; x; x -= lb (x)) ret += t[x]; return ret; }  
    int qry_kth (int u) {
        int ans = 0;
        int l = 1, r = n;
        while (l <= r) {
            int mid = l + r >> 1;
            if (qry (mid) == u) ans = mid, r = mid - 1;
            else if (qry (mid) > u) r = mid - 1;
            else if (qry (mid) < u) l = mid + 1;
        }
        return ans;
    }
    int qry_kth_ (int u) {
        int pos = 0, np;
        for (int i = 21; ~i; i --) {
            if ((np = pos | (1 << i)) <= n && t[np] < u)
                pos = np, u -= t[np];
                
        }
        return pos + 1;
    }
} t;

int main (void) {

    t.init (3e6); for (int i = 1; i <= 3e6; i ++) t.add (i, 1);
    int q; scanf ("%d", &q); 
    while (q --) {
        int u, v; scanf ("%d%d", &u, &v);
        if (u <= 3e6 && !mn[u]) for (int i = u; i <= 3e6; i += u) if (!mn[i]) t.add (i, -1), mn[i] = 1;
        printf ("%d\n", t.qry_kth_ (v));
    }

    return 0;
}