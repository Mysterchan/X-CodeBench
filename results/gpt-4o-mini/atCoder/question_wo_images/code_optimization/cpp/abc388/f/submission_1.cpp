#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool canReach(long long N, int M, int A, int B, const vector<pair<long long, long long>>& bad_intervals) {
    vector<bool> is_bad(N + 1, false);
    
    // Mark bad squares
    for (const auto& interval : bad_intervals) {
        for (long long j = interval.first; j <= interval.second && j <= N; ++j) {
            is_bad[j] = true;
        }
    }

    // Using a dynamic programming-like approach to check reachable squares
    long long last_reachable = 1; // We start at square 1

    for (long long current_square = 1; current_square <= last_reachable && current_square <= N; ++current_square) {
        if (is_bad[current_square]) continue; // If the current square is bad, skip it

        // Try all moves from current_square
        for (int i = A; i <= B; ++i) {
            long long next_square = current_square + i;
            if (next_square > N) break; // No need to check beyond N

            if (!is_bad[next_square]) {
                last_reachable = max(last_reachable, next_square); // Update the last reachable square
            }
        }

        // If we can directly reach N
        if (last_reachable >= N) return true;
    }

    return false;
}

int main() {
    long long N;
    int M, A, B;
    cin >> N >> M >> A >> B;
    
    vector<pair<long long, long long>> bad_intervals(M);
    
    for (int i = 0; i < M; ++i) {
        cin >> bad_intervals[i].first >> bad_intervals[i].second;
    }
    
    cout << (canReach(N, M, A, B, bad_intervals) ? "Yes" : "No") << endl;
    
    return 0;
}