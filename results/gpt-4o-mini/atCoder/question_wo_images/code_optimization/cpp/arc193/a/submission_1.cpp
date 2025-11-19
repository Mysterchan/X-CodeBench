#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Interval {
    int L, R, index;
};

bool compareIntervals(const Interval &a, const Interval &b) {
    return a.L < b.L;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<ll> W(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> W[i];
    }

    vector<Interval> intervals(N);
    for (int i = 1; i <= N; i++) {
        cin >> intervals[i - 1].L >> intervals[i - 1].R;
        intervals[i - 1].index = i;
    }

    sort(intervals.begin(), intervals.end(), compareIntervals);

    vector<vector<int>> graph(N + 1);
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (intervals[i].R < intervals[j].L) break; // No intersection
            if (!(intervals[i].R < intervals[j].L)) {
                graph[intervals[i].index].push_back(intervals[j].index);
                graph[intervals[j].index].push_back(intervals[i].index);
                if (intervals[j].R < intervals[i].L) break; // No intersection
            }
        }
    }

    int Q;
    cin >> Q;

    while (Q--) {
        int s, t;
        cin >> s >> t;

        vector<ll> dist(N + 1, LLONG_MAX);
        dist[s] = W[s];
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;
        pq.push({dist[s], s});

        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();

            if (d > dist[u]) continue;

            for (int v : graph[u]) {
                ll new_dist = d + W[v];
                if (new_dist < dist[v]) {
                    dist[v] = new_dist;
                    pq.push({new_dist, v});
                }
            }
        }

        cout << (dist[t] == LLONG_MAX ? -1 : dist[t]) << "\n";
    }

    return 0;
}
