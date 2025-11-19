#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int n;
    string s;
    cin >> n >> s;

    vector<int> positions;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') {
            positions.push_back(i);
        }
    }

    int k = positions.size();
    int median_index = k / 2; // This gives us the median position
    long long min_operations = 0;

    for (int i = 0; i < k; i++) {
        // We want all 1's to be at positions around the median
        min_operations += abs(positions[i] - (positions[median_index] + (i - median_index)));
    }

    cout << min_operations << '\n';
    return 0;
}