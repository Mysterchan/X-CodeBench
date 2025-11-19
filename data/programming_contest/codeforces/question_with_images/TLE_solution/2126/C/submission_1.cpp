
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool canReach(vector<long long>& h, int start, long long max_height, int current_time, vector<bool>& visited) {
    if (h[start] == max_height) return true;
    
    visited[start] = true;
    
    for (int i = 0; i < h.size(); i++) {
        if (i == start || visited[i]) continue;
        
        long long teleport_time = abs(h[start] - h[i]);
        long long arrival_time = current_time + teleport_time;
        
        bool can_survive_teleport = (arrival_time <= h[start]);
        
        bool can_survive_arrival = (1 + arrival_time <= h[i]);
        
        if (can_survive_teleport && can_survive_arrival) {
            if (canReach(h, i, max_height, arrival_time, visited)) {
                visited[start] = false;
                return true;
            }
        }
    }
    
    visited[start] = false;
    return false;
}

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n, k;
        cin >> n >> k;
        k--;
        
        vector<long long> h(n);
        for (int i = 0; i < n; i++) {
            cin >> h[i];
        }
        
        long long max_height = *max_element(h.begin(), h.end());
        
        if (h[k] == max_height) {
            cout << "YES\n";
            continue;
        }
        
        vector<bool> visited(n, false);
        bool possible = canReach(h, k, max_height, 0, visited);
        
        cout << (possible ? "YES" : "NO") << "\n";
    }
    
    return 0;
}
