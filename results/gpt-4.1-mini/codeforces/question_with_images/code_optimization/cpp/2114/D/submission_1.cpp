#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

void test() {
    int n;
    cin >> n;
    vector<pair<int, int>> points(n);

    int min_x = LLONG_MAX, max_x = LLONG_MIN;
    int min_y = LLONG_MAX, max_y = LLONG_MIN;

    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
        min_x = min(min_x, points[i].first);
        max_x = max(max_x, points[i].first);
        min_y = min(min_y, points[i].second);
        max_y = max(max_y, points[i].second);
    }

    if (n == 1) {
        cout << 1 << '\n';
        return;
    }

    // Count how many points are on each boundary
    int left_count = 0, right_count = 0, top_count = 0, bottom_count = 0;
    for (auto &p : points) {
        if (p.first == min_x) left_count++;
        if (p.first == max_x) right_count++;
        if (p.second == min_y) bottom_count++;
        if (p.second == max_y) top_count++;
    }

    // Candidates are points on any boundary
    // We only need to consider points on boundaries because moving an internal point won't reduce the bounding rectangle
    // Collect indices of candidates
    vector<int> candidates;
    for (int i = 0; i < n; i++) {
        auto &p = points[i];
        if (p.first == min_x || p.first == max_x || p.second == min_y || p.second == max_y) {
            candidates.push_back(i);
        }
    }

    int ans = LLONG_MAX;

    // Precompute min and max for x and y arrays for all points
    // We'll try removing each candidate and compute bounding box of remaining points
    // To do this efficiently, we can precompute prefix and suffix min/max arrays for x and y sorted by x and y

    // Sort points by x and y separately
    vector<pair<int,int>> by_x = points;
    vector<pair<int,int>> by_y = points;
    sort(by_x.begin(), by_x.end());
    sort(by_y.begin(), by_y.end(), [](auto &a, auto &b){ return a.second < b.second; });

    // Create maps from point to index in by_x and by_y for O(1) lookup
    unordered_map<int,int> idx_in_x(n), idx_in_y(n);
    // We'll store indices by original order
    // But since points are distinct, we can store their positions in by_x and by_y
    // To do this, we can store a map from point to index
    // But points can be large, so we can store a map from pair to index using a hash

    // Use a hash map from pair to index
    // Since coordinates can be large, use a custom hash
    struct pair_hash {
        size_t operator()(const pair<int,int> &p) const {
            return p.first * 1000000007LL + p.second;
        }
    };

    unordered_map<pair<int,int>, int, pair_hash> pos_in_x, pos_in_y;
    for (int i = 0; i < n; i++) {
        pos_in_x[by_x[i]] = i;
        pos_in_y[by_y[i]] = i;
    }

    // Precompute prefix and suffix min/max for x and y
    // For by_x:
    vector<int> prefix_min_y(n), prefix_max_y(n), suffix_min_y(n), suffix_max_y(n);
    prefix_min_y[0] = by_x[0].second;
    prefix_max_y[0] = by_x[0].second;
    for (int i = 1; i < n; i++) {
        prefix_min_y[i] = min(prefix_min_y[i-1], by_x[i].second);
        prefix_max_y[i] = max(prefix_max_y[i-1], by_x[i].second);
    }
    suffix_min_y[n-1] = by_x[n-1].second;
    suffix_max_y[n-1] = by_x[n-1].second;
    for (int i = n-2; i >= 0; i--) {
        suffix_min_y[i] = min(suffix_min_y[i+1], by_x[i].second);
        suffix_max_y[i] = max(suffix_max_y[i+1], by_x[i].second);
    }

    // For by_y:
    vector<int> prefix_min_x(n), prefix_max_x(n), suffix_min_x(n), suffix_max_x(n);
    prefix_min_x[0] = by_y[0].first;
    prefix_max_x[0] = by_y[0].first;
    for (int i = 1; i < n; i++) {
        prefix_min_x[i] = min(prefix_min_x[i-1], by_y[i].first);
        prefix_max_x[i] = max(prefix_max_x[i-1], by_y[i].first);
    }
    suffix_min_x[n-1] = by_y[n-1].first;
    suffix_max_x[n-1] = by_y[n-1].first;
    for (int i = n-2; i >= 0; i--) {
        suffix_min_x[i] = min(suffix_min_x[i+1], by_y[i].first);
        suffix_max_x[i] = max(suffix_max_x[i+1], by_y[i].first);
    }

    // Function to get bounding box after removing one point
    auto bounding_box_after_removal = [&](int idx) {
        // idx is index in original points
        auto p = points[idx];

        // Find position in by_x and by_y
        int pos_x = pos_in_x[p];
        int pos_y = pos_in_y[p];

        // Compute min_x and max_x after removal
        int cur_min_x, cur_max_x;
        if (pos_x == 0) {
            cur_min_x = by_x[1].first;
        } else {
            cur_min_x = by_x[0].first;
        }
        if (pos_x == n-1) {
            cur_max_x = by_x[n-2].first;
        } else {
            cur_max_x = by_x[n-1].first;
        }
        if (pos_x > 0 && pos_x < n-1) {
            cur_min_x = min(by_x[0].first, by_x[1].first);
            cur_max_x = max(by_x[n-1].first, by_x[n-2].first);
            // Actually, since by_x is sorted, min_x is by_x[0].first unless we remove it
            // So if pos_x != 0, min_x = by_x[0].first
            // if pos_x != n-1, max_x = by_x[n-1].first
            // So above is correct
        }

        // Compute min_y and max_y after removal
        int cur_min_y, cur_max_y;
        if (pos_y == 0) {
            cur_min_y = by_y[1].second;
        } else {
            cur_min_y = by_y[0].second;
        }
        if (pos_y == n-1) {
            cur_max_y = by_y[n-2].second;
        } else {
            cur_max_y = by_y[n-1].second;
        }

        // But we need to consider the y range of points excluding the removed one
        // We can get min_y and max_y from prefix and suffix arrays for by_x and by_y

        // For x range:
        int min_x_after = (pos_x == 0) ? by_x[1].first : by_x[0].first;
        int max_x_after = (pos_x == n-1) ? by_x[n-2].first : by_x[n-1].first;

        // For y range:
        // For by_x, y range excluding pos_x:
        int min_y_after, max_y_after;
        if (pos_x == 0) {
            min_y_after = suffix_min_y[1];
            max_y_after = suffix_max_y[1];
        } else if (pos_x == n-1) {
            min_y_after = prefix_min_y[n-2];
            max_y_after = prefix_max_y[n-2];
        } else {
            min_y_after = min(prefix_min_y[pos_x-1], suffix_min_y[pos_x+1]);
            max_y_after = max(prefix_max_y[pos_x-1], suffix_max_y[pos_x+1]);
        }

        // Similarly for y range from by_y:
        int min_x_after_y, max_x_after_y;
        if (pos_y == 0) {
            min_x_after_y = suffix_min_x[1];
            max_x_after_y = suffix_max_x[1];
        } else if (pos_y == n-1) {
            min_x_after_y = prefix_min_x[n-2];
            max_x_after_y = prefix_max_x[n-2];
        } else {
            min_x_after_y = min(prefix_min_x[pos_y-1], suffix_min_x[pos_y+1]);
            max_x_after_y = max(prefix_max_x[pos_y-1], suffix_max_x[pos_y+1]);
        }

        // The bounding box after removal must contain all points except the removed one
        // So min_x_after and max_x_after from by_x are correct for x
        // min_y_after and max_y_after from by_x are correct for y

        // But we must ensure the bounding box covers all points except the removed one
        // So we take min_x_after and max_x_after from by_x
        // min_y_after and max_y_after from by_x

        // The rectangle area:
        int length = max_x_after - min_x_after + 1;
        int width = max_y_after - min_y_after + 1;
        int area = length * width;

        // Check if area == n-1 (number of points after removal)
        // If yes, we can try to expand rectangle by 1 in either direction to include the moved monster
        if (area == n - 1) {
            // Try expanding length or width by 1
            int area1 = (length + 1) * width;
            int area2 = length * (width + 1);
            area = min(area1, area2);
        }

        return area;
    };

    for (auto c : candidates) {
        int cur_area = bounding_box_after_removal(c);
        if (cur_area < ans) ans = cur_area;
    }

    cout << ans << '\n';
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) test();
    return 0;
}