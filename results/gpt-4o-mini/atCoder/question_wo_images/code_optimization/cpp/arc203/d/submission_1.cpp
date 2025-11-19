#include <bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(false), cin.tie(0)

const int N = 200005;
int a[N];
int n;

int countSegments() {
    int count = 0; // will hold the count of segments
    for (int i = 1; i < n; ++i) {
        if (a[i] == 0 && a[i + 1] == 0) {
            count++;
        }
    }
    return count;
}

void updateSegmentCounts(set<int> &segments, int idx) {
    if (a[idx] == 1) return; // if we are turning a 1 into a 0, only check segments involving idx
    if (idx > 1 && a[idx - 1] == 0 && a[idx] == 0) {
        segments.erase(idx - 1);
    }
    if (idx < n && a[idx] == 0 && a[idx + 1] == 0) {
        segments.erase(idx);
    }
    if (idx > 1 && a[idx - 1] == 0 && a[idx] == 1) {
        segments.insert(idx - 1);
    }
    if (idx < n && a[idx] == 1 && a[idx + 1] == 0) {
        segments.insert(idx);
    }
}

int main() {
    fastio;
    
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    set<int> segments;
    for (int i = 1; i < n; ++i) {
        if (a[i] == 0 && a[i + 1] == 0) {
            segments.insert(i);
        }
    }

    int totalSegments = countSegments();
    
    int q;
    cin >> q;
    while (q--) {
        int i;
        cin >> i;
        a[i] ^= 1;

        // Update totalSegments based on the flip
        updateSegmentCounts(segments, i);
        
        // Recount segments after change
        totalSegments = countSegments();
        
        // The minimum size of B
        cout << n - totalSegments << "\n"; // Minimum length of B
    }
    
    return 0;
}
