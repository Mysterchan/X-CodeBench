#include <bits/stdc++.h>
using namespace std;

const int N = 5e5 + 10;
int sizes[N];
int fa[N];
int depth[N];
int T;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> T;
    while (T--) {
        int n;
        cin >> n;

        // Reset sizes for current test case
        for (int i = 1; i <= n; i++) sizes[i] = 0;

        depth[1] = 1;
        for (int i = 2; i <= n; i++) {
            cin >> fa[i];
            sizes[fa[i]]++;
            depth[i] = depth[fa[i]] + 1;
        }

        // Use a priority queue to store leaves by depth
        priority_queue<pair<int, int>> q;
        for (int i = 1; i <= n; i++) {
            if (sizes[i] == 0) {
                q.emplace(depth[i], i);
            }
        }

        int ans = 0;
        while ((int)q.size() >= 2) {
            auto a = q.top(); q.pop();
            auto b = q.top(); q.pop();
            ans++;

            int x = fa[a.second], y = fa[b.second];
            sizes[x]--;
            if (sizes[x] == 0) q.emplace(depth[x], x);
            sizes[y]--;
            if (sizes[y] == 0) q.emplace(depth[y], y);
        }

        cout << ans << "\n";
    }

    return 0;
}