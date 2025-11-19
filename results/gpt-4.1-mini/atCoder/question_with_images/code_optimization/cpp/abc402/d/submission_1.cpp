#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Fenwick {
    int n;
    vector<int> bit;
    Fenwick(int n): n(n), bit(n+1,0) {}
    void update(int i, int v) {
        for (; i <= n; i += i & -i) bit[i] += v;
    }
    int query(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) s += bit[i];
        return s;
    }
    int query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l-1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<pair<int,int>> chords(M);
    for (int i = 0; i < M; i++) {
        int a, b; cin >> a >> b;
        if (a > b) swap(a, b);
        chords[i] = {a, b};
    }

    // Sort chords by their left endpoint
    sort(chords.begin(), chords.end());

    // We want to count pairs of chords that intersect.
    // Two chords (a,b) and (c,d) with a < c intersect iff a < c < b < d.
    // So for chords sorted by a, count how many chords have b < d for c > a and b > c.

    // We'll process chords in order of increasing a.
    // For each chord, count how many chords processed so far have b > current b.
    // This is equivalent to counting inversions on the b's.

    Fenwick fenw(N);
    ll ans = 0;
    for (auto &ch : chords) {
        int b = ch.second;
        // Number of chords with b > current b = total processed - number with b <= current b
        int smaller_or_equal = fenw.query(b);
        int processed = fenw.query(N);
        ans += (processed - smaller_or_equal);
        fenw.update(b, 1);
    }

    cout << ans << "\n";
    return 0;
}