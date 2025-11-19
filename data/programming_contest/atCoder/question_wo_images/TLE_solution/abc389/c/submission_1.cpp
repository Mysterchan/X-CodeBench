#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int q;
    long long head = 0, tail;
    cin >> q;
    deque<deque<long long>> queue;

    while (q--) {
        int type;
        cin >> type;

        if (type == 1) {
            long long l; cin >> l;
            tail = head + l;

            queue.push_back({head, tail});
            head = tail;
        }
        else if (type == 2) {
            long long m = queue.front().back() - queue.front().front();
            queue.pop_front();
            for (int i = 0, len = queue.size(); i < len; i++) {
                queue[i].front() = queue[i].front() - m;
                queue[i].back() = queue[i].back() - m;
            }
            head -= m;
        }
        else {
            long long k; cin >> k;
            cout << queue[k - 1].front() << endl;
        }
    }
    return 0;
}