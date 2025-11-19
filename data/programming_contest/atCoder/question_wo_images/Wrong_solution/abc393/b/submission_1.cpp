#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        sort(a.begin(), a.end());
        a.erase(unique(a.begin(), a.end()), a.end());
        int m = a.size();
        vector<pair<int, int>> events;
        for (int i = 0; i < m; i++) {
            events.push_back({a[i] + 1, 1});
            events.push_back({a[i] + n + 1, -1});
        }
        sort(events.begin(), events.end());
        int current = 0;
        int ans = 0;
        for (auto event : events) {
            current += event.second;
            if (current > ans) {
                ans = current;
            }
        }
        cout << ans << endl;
    }
    return 0;
}