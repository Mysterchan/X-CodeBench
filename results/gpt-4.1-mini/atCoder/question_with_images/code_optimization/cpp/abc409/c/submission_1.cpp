#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, l;
    cin >> n >> l;
    vector<int> d(n - 1);
    for (int i = 0; i < n - 1; i++) cin >> d[i];

    if (l % 3 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    int length = l / 3;
    int length2 = 2 * length;

    // Compute positions of points on the circle
    vector<int> pos(n);
    pos[0] = 0;
    int s = 0;
    for (int i = 0; i < n - 1; i++) {
        s += d[i];
        if (s >= l) s -= l;
        pos[i + 1] = s;
    }

    // Group points by their position modulo l
    // Since positions are modulo l, and l can be large,
    // we use a vector of vectors indexed by position.
    // But we only need to access positions i, i+length, i+length2 modulo l.
    // So we create a vector of vectors for all positions.
    vector<vector<int>> p(l);
    for (int i = 0; i < n; i++) {
        p[pos[i]].push_back(i);
    }

    long long result = 0;

    // For each i in [0, length-1], check triples at positions i, i+length, i+length2
    // We want to count triples (a,b,c) with a < b < c and points at these positions.
    // The original code triple nested loops over all points at these positions is O(N^3) worst.
    // We optimize by sorting the indices at each position and counting the number of triples
    // with a < b < c using a three-pointer approach or counting pairs efficiently.

    // Since the points at each position are sorted by their indices (because we inserted in order),
    // we can use a three-pointer approach or count pairs efficiently.

    // For each i:
    // Let A = p[i], B = p[(i+length)%l], C = p[(i+length2)%l]
    // We want to count number of triples (a,b,c) with a in A, b in B, c in C and a < b < c.

    for (int i = 0; i < length; i++) {
        int j = i + length;
        if (j >= l) j -= l;
        int k = i + length2;
        if (k >= l) k -= l;

        const auto &A = p[i];
        const auto &B = p[j];
        const auto &C = p[k];

        if (A.empty() || B.empty() || C.empty()) continue;

        // We want to count triples (a,b,c) with a < b < c
        // For fixed b in B, count number of a in A with a < b and number of c in C with c > b
        // Then sum over b: count_a * count_c

        // Since A, B, C are sorted, we can do binary searches.

        // Precompute sizes
        int sizeA = (int)A.size();
        int sizeC = (int)C.size();

        for (int b : B) {
            // count of a in A with a < b
            int count_a = (int)(std::lower_bound(A.begin(), A.end(), b) - A.begin());
            // count of c in C with c > b
            int count_c = (int)(C.end() - std::upper_bound(C.begin(), C.end(), b));
            result += (long long)count_a * count_c;
        }
    }

    cout << result << "\n";
    return 0;
}