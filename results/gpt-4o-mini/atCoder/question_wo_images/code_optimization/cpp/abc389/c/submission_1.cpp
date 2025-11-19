#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int q;
    long long head_offset = 0;
    vector<long long> queue;

    cin >> q;
    while (q--) {
        int type;
        cin >> type;

        if (type == 1) {
            long long l; 
            cin >> l;
            queue.push_back(head_offset + (queue.empty() ? 0 : queue.back()));
            head_offset += l;
        }
        else if (type == 2) {
            long long m = queue.front() - head_offset;
            queue.erase(queue.begin());
            head_offset += m;
        }
        else {
            long long k; 
            cin >> k;
            cout << queue[k - 1] - head_offset << endl;
        }
    }
    return 0;
}