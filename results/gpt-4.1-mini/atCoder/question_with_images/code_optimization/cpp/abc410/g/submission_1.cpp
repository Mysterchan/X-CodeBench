#include <bits/stdc++.h>
using namespace std;
#define ll long long

struct Chord {
    int l, r;
    bool operator<(const Chord &c) const {
        return l < c.l;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    vector<Chord> chords(N);
    for (int i = 0; i < N; i++) {
        int A, B; cin >> A >> B;
        if (A > B) swap(A, B);
        chords[i] = {A, B};
    }

    // Sort chords by left endpoint
    sort(chords.begin(), chords.end());

    // We want to find the size of the maximum set of non-intersecting chords (maximum independent set)
    // on the circle, which is equivalent to finding the maximum chain of chords that do not intersect.
    // Then, after deleting chords to get this set, we add one chord that intersects all chords in the set,
    // so the maximum number of intersections is size_of_max_independent_set.

    // To find the maximum number of non-intersecting chords, we can find the length of the longest chain
    // where chords are sorted by left endpoint and the right endpoints are strictly increasing.
    // This is equivalent to finding the length of the Longest Increasing Subsequence (LIS) of the right endpoints.

    vector<int> rights;
    for (auto &c : chords) rights.push_back(c.r);

    // Compute LIS on rights
    vector<int> lis;
    for (int x : rights) {
        // Use binary search to find position to replace or append
        auto it = lower_bound(lis.begin(), lis.end(), x);
        if (it == lis.end()) lis.push_back(x);
        else *it = x;
    }

    // The maximum number of intersections after operations is the size of this LIS
    cout << (int)lis.size() << "\n";

    return 0;
}