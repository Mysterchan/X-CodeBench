#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    // We will maintain the drawn chords in a balanced structure.
    // The key insight:
    // Two chords (a,b) and (c,d) with a < b and c < d intersect iff:
    // a < c < b < d or c < a < d < b.
    // Since all endpoints are distinct, we can store chords by their left endpoint.
    // For each new chord (x,y), we check if it intersects any existing chord.
    // Because chords are stored sorted by left endpoint, we only need to check
    // the chord with the smallest left endpoint >= x (upper_bound)
    // and the chord with the largest left endpoint < x (prev iterator).
    // If either intersects, we reject the chord.

    // Store chords as pairs (left_endpoint, right_endpoint)
    // left_endpoint < right_endpoint guaranteed by input constraints.
    set<pair<int,int>> chords;

    for (int _ = 0; _ < Q; _++) {
        int A, B;
        cin >> A >> B;
        if (A > B) swap(A, B);

        // Find the first chord with left endpoint >= A
        auto it = chords.lower_bound({A, -1});
        bool intersect = false;

        // Check chord at it
        if (it != chords.end()) {
            int c = it->first, d = it->second;
            // Check if (A,B) intersects (c,d)
            // intersect if A < c < B < d
            if (A < c && c < B && B < d) {
                intersect = true;
            }
        }

        // Check chord before it
        if (!intersect && it != chords.begin()) {
            --it;
            int c = it->first, d = it->second;
            // Check if (A,B) intersects (c,d)
            // intersect if c < A < d < B
            if (c < A && A < d && d < B) {
                intersect = true;
            }
        }

        if (intersect) {
            cout << "No\n";
        } else {
            chords.insert({A, B});
            cout << "Yes\n";
        }
    }

    return 0;
}