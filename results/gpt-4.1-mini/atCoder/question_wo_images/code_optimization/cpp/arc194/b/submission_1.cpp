#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Fenwick {
    int n;
    vector<ll> bit;
    Fenwick(int n) : n(n), bit(n + 1, 0) {}
    void update(int i, ll v) {
        for (; i <= n; i += i & -i) bit[i] += v;
    }
    ll query(int i) {
        ll s = 0;
        for (; i > 0; i -= i & -i) s += bit[i];
        return s;
    }
    ll query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    vector<int> P(n + 1);
    for (int i = 1; i <= n; i++) cin >> P[i];

    Fenwick fenw_pos(n), fenw_count(n);
    ll res = 0;

    // Process from left to right
    // For each element P[i], 
    // cost contributed by inversions with elements before i is:
    // number of elements before i with value > P[i] * i
    // but since cost depends on position of swap, we use Fenwicks to sum positions of elements > P[i]

    for (int i = 1; i <= n; i++) {
        // sum of positions of elements > P[i] seen so far
        ll sum_pos_greater = fenw_pos.query(P[i] + 1, n);
        // number of elements > P[i] seen so far
        ll count_greater = fenw_count.query(P[i] + 1, n);
        // cost contribution for current element
        // Each inversion contributes cost equal to the position of the smaller element in the swap
        // The cost for swapping P[i] past all greater elements before it is sum of their positions
        // minus count_greater * i (because swaps happen at positions less than i)
        // Actually, the minimal cost is sum of positions of greater elements before i
        // minus count_greater * i, but since cost is i for swapping at position i,
        // the total cost is sum_pos_greater - count_greater * i
        // But this is the cost of moving P[i] to the left past all greater elements.
        // Actually, the problem states cost of swapping at position i is i,
        // so when swapping P_j and P_{j+1}, cost is j.
        // To move P[i] left past all greater elements before it,
        // total cost is sum of positions of those greater elements (their indices),
        // minus count_greater * i (because each swap moves P[i] one step left, cost is position of swap)
        // But this is complicated, so let's use the known formula:
        // The minimal total cost = sum over all inversions of the smaller index in the pair.
        // For inversion (i,j) with i<j and P[i]>P[j], cost is i.
        // So for each element, sum over all greater elements before it of their positions.
        // So we accumulate sum of positions of greater elements before i.

        // Actually, the cost is sum of positions of the smaller index in each inversion.
        // For inversion (i,j) with i<j and P[i]>P[j], cost is i.
        // So for each element P[j], the cost contributed is sum of i over all i<j with P[i]>P[j].
        // So for each P[j], cost += sum of positions i of greater elements before j.

        res += sum_pos_greater;

        // Update Fenwicks with current element
        fenw_pos.update(P[i], i);
        fenw_count.update(P[i], 1);
    }

    cout << res << '\n';

    return 0;
}