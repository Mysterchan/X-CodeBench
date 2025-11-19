#include <iostream>
#include <queue>
#include <vector>
#include <set>

using namespace std;

bool is_bad(long long square, const vector<pair<long long, long long>>& bad_intervals) {
    for (const auto& interval : bad_intervals) {
        if (square >= interval.first && square <= interval.second) {
            return true;
        }
    }
    return false;
}

string is_possible_to_move(long long N, int M, int A, int B, const vector<pair<long long, long long>>& bad_intervals) {
    queue<long long> q;
    set<long long> visited;
    
    q.push(1);
    visited.insert(1);
    
    while (!q.empty()) {
        long long current_square = q.front();
        q.pop();
        
        for (int i = A; i <= B; ++i) {
            long long next_square = current_square + i;
            
            if (next_square > N) {
                break;
            }
            
            if (visited.find(next_square) == visited.end() && !is_bad(next_square, bad_intervals)) {
                if (next_square == N) {
                    return "Yes";
                }
                visited.insert(next_square);
                q.push(next_square);
            }
        }
    }
    
    return "No";
}

int main() {
    long long N;
    int M, A, B;
    cin >> N >> M >> A >> B;
    
    vector<pair<long long, long long>> bad_intervals(M);
    
    for (int i = 0; i < M; ++i) {
        cin >> bad_intervals[i].first >> bad_intervals[i].second;
    }
    
    cout << is_possible_to_move(N, M, A, B, bad_intervals) << endl;
    
    return 0;
}
