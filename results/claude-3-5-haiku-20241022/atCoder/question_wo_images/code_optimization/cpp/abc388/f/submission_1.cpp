#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    long long N;
    int M, A, B;
    cin >> N >> M >> A >> B;
    
    vector<pair<long long, long long>> bad_intervals(M);
    for (int i = 0; i < M; ++i) {
        cin >> bad_intervals[i].first >> bad_intervals[i].second;
    }
    
    set<long long> reachable;
    reachable.insert(1);
    
    long long current_max = 1;
    
    for (int idx = 0; idx < M; ++idx) {
        long long L = bad_intervals[idx].first;
        long long R = bad_intervals[idx].second;
        
        // Check if we can reach past this interval
        if (current_max + B < L) {
            // Can't reach this interval at all
            cout << "No" << endl;
            return 0;
        }
        
        // Try to find positions that can jump over the interval
        set<long long> new_reachable;
        long long new_max = current_max;
        
        // Check positions in reachable set
        for (long long pos : reachable) {
            if (pos > R) {
                new_reachable.insert(pos);
                new_max = max(new_max, pos);
                continue;
            }
            
            // Try jumps from this position
            for (int jump = A; jump <= B; ++jump) {
                long long next = pos + jump;
                if (next > N) break;
                if (next > R) {
                    new_reachable.insert(next);
                    new_max = max(new_max, next);
                }
            }
        }
        
        // Add positions just before the interval that might help
        for (long long pos = max(1LL, L - B); pos < L; ++pos) {
            if (pos <= current_max) {
                for (int jump = A; jump <= B; ++jump) {
                    long long next = pos + jump;
                    if (next > N) break;
                    if (next > R) {
                        new_reachable.insert(next);
                        new_max = max(new_max, next);
                    }
                }
            }
        }
        
        if (new_max <= R) {
            cout << "No" << endl;
            return 0;
        }
        
        reachable = new_reachable;
        current_max = new_max;
        
        // Keep only relevant positions (within B of next interval or close to current max)
        if (idx + 1 < M) {
            long long next_L = bad_intervals[idx + 1].first;
            set<long long> filtered;
            for (long long pos : reachable) {
                if (pos >= current_max - B || pos >= next_L - B) {
                    filtered.insert(pos);
                }
            }
            reachable = filtered;
        }
    }
    
    // Check if we can reach N from current positions
    if (current_max + B >= N) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    
    return 0;
}