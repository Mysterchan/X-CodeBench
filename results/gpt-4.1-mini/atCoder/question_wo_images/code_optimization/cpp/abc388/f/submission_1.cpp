#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    int M, A, B;
    cin >> N >> M >> A >> B;

    vector<pair<long long, long long>> bad_intervals(M);
    for (int i = 0; i < M; ++i) {
        cin >> bad_intervals[i].first >> bad_intervals[i].second;
    }

    // Add sentinel intervals at start and end to simplify processing
    // The problem states 1 < L_i, R_i < N, so no bad intervals at 1 or N
    // We'll consider the "good" intervals between bad intervals and edges

    // We'll process intervals of good squares (not bad)
    // good intervals are:
    // [1, L_1 - 1], [R_1 + 1, L_2 - 1], ..., [R_M + 1, N]

    // If M == 0, whole [1, N] is good
    // We'll store good intervals as pairs (start, end)
    vector<pair<long long, long long>> good_intervals;

    long long prev_end = 0;
    for (int i = 0; i < M; ++i) {
        long long start_good = prev_end + 1;
        long long end_good = bad_intervals[i].first - 1;
        if (start_good <= end_good) {
            good_intervals.emplace_back(start_good, end_good);
        }
        prev_end = bad_intervals[i].second;
    }
    // Last good interval after last bad interval
    if (prev_end < N) {
        good_intervals.emplace_back(prev_end + 1, N);
    }

    // If the first square (1) is bad, no solution
    // But problem states 1 < L_i, so 1 is always good

    // We'll keep track of reachable positions as intervals within good intervals
    // Initially, reachable interval is [1,1]
    // We'll process good intervals in order, trying to propagate reachability

    // dp_intervals: vector of pairs representing reachable intervals within each good interval
    // Initially empty, we will build it as we go

    // We'll process good intervals one by one, maintaining the reachable intervals within them

    // For the first good interval, if it contains 1, reachable interval is [1,1]
    // else no reachable positions

    vector<pair<long long, long long>> reachable_intervals;

    // Find the good interval containing 1
    int idx = -1;
    for (int i = 0; i < (int)good_intervals.size(); ++i) {
        if (good_intervals[i].first <= 1 && 1 <= good_intervals[i].second) {
            idx = i;
            break;
        }
    }
    if (idx == -1) {
        // 1 is bad, no solution
        cout << "No\n";
        return 0;
    }

    // Initialize reachable intervals with [1,1] in good_intervals[idx]
    reachable_intervals.resize(good_intervals.size(), make_pair(-1LL, -1LL));
    reachable_intervals[idx] = {1, 1};

    // We'll process intervals from idx to end
    // For each good interval i, if reachable_intervals[i] is empty, skip
    // From reachable_intervals[i], we can jump A..B steps to next positions
    // These next positions may be in the same good interval or in subsequent good intervals

    // To efficiently propagate reachability, we use a two-pointer approach over good intervals

    // Precompute prefix sums of good intervals lengths for binary search if needed
    // But here linear scan is enough since M <= 2e4

    for (int i = idx; i < (int)good_intervals.size(); ++i) {
        if (reachable_intervals[i].first == -1) continue; // no reachable positions here

        long long reach_start = reachable_intervals[i].first;
        long long reach_end = reachable_intervals[i].second;
        long long good_start = good_intervals[i].first;
        long long good_end = good_intervals[i].second;

        // From reachable positions [reach_start, reach_end], we can jump A..B steps
        // So next reachable positions are in [reach_start + A, reach_end + B]

        long long next_start = reach_start + A;
        long long next_end = reach_end + B;

        // We need to distribute [next_start, next_end] into good intervals starting from i (including i)
        // Because jumps can land in the same good interval or later ones

        // We'll iterate over good intervals starting from i
        for (int j = i; j < (int)good_intervals.size(); ++j) {
            long long gs = good_intervals[j].first;
            long long ge = good_intervals[j].second;

            // Intersection of [next_start, next_end] and [gs, ge]
            long long inter_start = max(next_start, gs);
            long long inter_end = min(next_end, ge);

            if (inter_start > inter_end) {
                // no intersection
                if (ge < next_start) {
                    // this good interval is before next_start, continue
                    continue;
                }
                if (gs > next_end) {
                    // intervals beyond next_end, break
                    break;
                }
                continue;
            }

            // Update reachable_intervals[j] with union of current and [inter_start, inter_end]
            if (reachable_intervals[j].first == -1) {
                reachable_intervals[j] = {inter_start, inter_end};
            } else {
                if (inter_start < reachable_intervals[j].first) reachable_intervals[j].first = inter_start;
                if (inter_end > reachable_intervals[j].second) reachable_intervals[j].second = inter_end;
            }
        }
    }

    // After propagation, check if N is reachable
    // Find which good interval contains N
    int pos = -1;
    for (int i = 0; i < (int)good_intervals.size(); ++i) {
        if (good_intervals[i].first <= N && N <= good_intervals[i].second) {
            pos = i;
            break;
        }
    }
    if (pos == -1) {
        // N is bad, no solution
        cout << "No\n";
        return 0;
    }

    if (reachable_intervals[pos].first != -1 && reachable_intervals[pos].first <= N && N <= reachable_intervals[pos].second) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}