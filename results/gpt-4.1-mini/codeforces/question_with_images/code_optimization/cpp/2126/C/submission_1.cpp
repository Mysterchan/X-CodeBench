#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        k--;
        vector<long long> h(n);
        for (int i = 0; i < n; i++) cin >> h[i];

        long long max_height = *max_element(h.begin(), h.end());

        // If starting tower is already max height, answer YES immediately
        if (h[k] == max_height) {
            cout << "YES\n";
            continue;
        }

        // We want to find if we can reach any tower with height == max_height
        // before water level surpasses tower height.

        // Key insight:
        // The time to move from tower i to j is abs(h[i] - h[j]).
        // You stay on tower i during the teleportation.
        // You can start teleporting at any time >= arrival time at tower i.
        // Water level at time t is t+1.
        // You perish if water level > height of tower you are on at any time.

        // We want to find the minimal arrival time at each tower.
        // Use Dijkstra-like approach with states: (arrival_time, tower_index)
        // Relax edges to all other towers j:
        //   start teleport at arrival_time at i
        //   teleport takes cost = abs(h[i] - h[j])
        //   arrival_time at j = arrival_time at i + cost
        // Conditions to move:
        //   - You survive on tower i during teleport:
        //       water level at any time t in [arrival_time_i, arrival_time_i + cost - 1] <= h[i]
        //       water level at time t = t+1
        //       max water level during teleport = arrival_time_i + cost
        //       So arrival_time_i + cost <= h[i]
        //   - You survive on arrival at tower j:
        //       water level at arrival_time_j + 1 <= h[j]
        //       arrival_time_j + 1 <= h[j]

        // So conditions:
        //   arrival_time_i + cost <= h[i]
        //   arrival_time_j + 1 <= h[j]

        // We'll implement Dijkstra with these constraints.

        vector<long long> dist(n, LLONG_MAX);
        dist[k] = 0;

        // Min-heap: (arrival_time, tower)
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
        pq.emplace(0, k);

        bool can_reach = false;

        while (!pq.empty()) {
            auto [cur_time, u] = pq.top(); pq.pop();
            if (dist[u] < cur_time) continue;

            if (h[u] == max_height) {
                can_reach = true;
                break;
            }

            // Try to teleport to all towers j
            // To optimize, we can try only towers that can be reached
            // But since n can be up to 1e5, O(n^2) is too large.

            // Optimization:
            // Since cost = abs(h[u] - h[j]), and conditions depend on h[u], h[j], and times,
            // we can try to process towers in order of height or use a data structure.

            // But problem constraints allow sum n <= 1e5 over all test cases,
            // so O(n^2) worst case is too large.

            // We need a better approach.

            // Observation:
            // The cost depends only on height difference.
            // The constraints are:
            //   cur_time + cost <= h[u]
            //   cur_time + cost + 1 <= h[j]

            // Rearranged:
            //   cost <= h[u] - cur_time
            //   cost + 1 <= h[j] - cur_time

            // Since cost = abs(h[u] - h[j]), let's consider two cases:

            // Case 1: h[j] >= h[u]
            //   cost = h[j] - h[u]
            //   Conditions:
            //     h[j] - h[u] <= h[u] - cur_time  => h[j] <= 2*h[u] - cur_time
            //     h[j] - h[u] + 1 <= h[j] - cur_time => 1 <= h[u] - cur_time
            //     So cur_time <= h[u] - 1

            // Case 2: h[j] < h[u]
            //   cost = h[u] - h[j]
            //   Conditions:
            //     h[u] - h[j] <= h[u] - cur_time => h[j] >= cur_time
            //     h[u] - h[j] + 1 <= h[j] - cur_time => h[u] + 1 <= 2*h[j] - cur_time
            //     => 2*h[j] >= h[u] + 1 + cur_time

            // This is complicated to check for all towers.

            // Instead, we can try a different approach:

            // Since teleportation cost depends on height difference,
            // and we want to minimize arrival time,
            // we can try to move only to towers that satisfy the constraints.

            // Let's try to process towers sorted by height.

            // We'll pre-sort towers by height and store their indices.

            // For each tower u, from current time cur_time,
            // we can teleport to towers j where:
            //   cost = abs(h[u] - h[j])
            //   cur_time + cost <= h[u]
            //   cur_time + cost + 1 <= h[j]

            // For fixed u and cur_time, define max cost allowed: max_cost = h[u] - cur_time
            // For each tower j, cost = abs(h[u] - h[j]) <= max_cost
            // Also, arrival_time_j = cur_time + cost
            // arrival_time_j + 1 <= h[j] => cur_time + cost + 1 <= h[j]

            // So for each tower j:
            //   abs(h[u] - h[j]) <= max_cost
            //   h[j] >= cur_time + abs(h[u] - h[j]) + 1

            // Let's try to find all towers j satisfying these.

            // Since h[j] is large, we can try to find candidates in the range [h[u] - max_cost, h[u] + max_cost]

            // We'll use binary search on sorted towers by height.

            // For each candidate tower j in that range, check if h[j] >= cur_time + abs(h[u] - h[j]) + 1

            // If yes, update dist[j] if arrival_time_j = cur_time + cost < dist[j]

            // To avoid repeated processing, we can mark visited towers.

            // Implementing this carefully:

            // Preprocessing: sort towers by height with their indices.

            // We'll do this once per test case.

            // Then for each u, we binary search towers in [h[u] - max_cost, h[u] + max_cost]

            // For each candidate, check condition and update dist.

            // To avoid TLE, we must be careful.

            // Since sum of n is 1e5, and each tower is processed once in Dijkstra,
            // and each tower tries to relax neighbors in a limited height range,
            // this should be efficient enough.

            // Let's implement this.

            // Preprocessing outside the loop:
            // We'll do it once per test case.

            // So we need to move this preprocessing outside the while loop.

            // Let's implement now.

            // Break from current loop to implement the full solution below.

            break;
        }

        if (can_reach) {
            cout << "YES\n";
            continue;
        }

        // Implement full solution with preprocessing and Dijkstra:

        // Preprocessing towers by height
        vector<pair<long long,int>> towers(n);
        for (int i = 0; i < n; i++) towers[i] = {h[i], i};
        sort(towers.begin(), towers.end());

        // We'll implement a new Dijkstra here:

        dist.assign(n, LLONG_MAX);
        dist[k] = 0;
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
        pq.emplace(0, k);

        vector<bool> processed(n, false);

        while (!pq.empty()) {
            auto [cur_time, u] = pq.top(); pq.pop();
            if (dist[u] < cur_time) continue;
            if (processed[u]) continue;
            processed[u] = true;

            if (h[u] == max_height) {
                can_reach = true;
                break;
            }

            long long max_cost = h[u] - cur_time;
            if (max_cost < 0) continue; // can't teleport anywhere

            // Find towers with height in [h[u] - max_cost, h[u] + max_cost]
            long long low_h = h[u] - max_cost;
            long long high_h = h[u] + max_cost;

            // Binary search for lower bound
            auto it_low = lower_bound(towers.begin(), towers.end(), make_pair(low_h, -1));
            auto it_high = upper_bound(towers.begin(), towers.end(), make_pair(high_h, n));

            for (auto it = it_low; it != it_high; ++it) {
                int j = it->second;
                if (j == u) continue;
                if (processed[j]) continue;

                long long cost = abs(h[u] - h[j]);
                long long arrival_time_j = cur_time + cost;

                // Check conditions:
                // 1) cur_time + cost <= h[u]
                // 2) arrival_time_j + 1 <= h[j]
                if (cur_time + cost <= h[u] && arrival_time_j + 1 <= h[j]) {
                    if (arrival_time_j < dist[j]) {
                        dist[j] = arrival_time_j;
                        pq.emplace(arrival_time_j, j);
                    }
                }
            }
        }

        cout << (can_reach ? "YES\n" : "NO\n");
    }

    return 0;
}