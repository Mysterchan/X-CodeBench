#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int q;
    cin >> q;
    
    deque<pair<long long, long long>> queue; // {original_head, length}
    long long offset = 0; // cumulative offset to subtract from all positions
    
    while (q--) {
        int type;
        cin >> type;

        if (type == 1) {
            long long l; 
            cin >> l;
            
            long long head;
            if (queue.empty()) {
                head = 0;
            } else {
                // Calculate position based on last snake's head + length
                head = queue.back().first + queue.back().second;
            }
            
            queue.push_back({head, l});
        }
        else if (type == 2) {
            long long m = queue.front().second;
            queue.pop_front();
            offset += m;
        }
        else {
            long long k; 
            cin >> k;
            cout << queue[k - 1].first - offset << endl;
        }
    }
    return 0;
}