#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;       // current run‐value
    int cnt;       // count of that run
    int id;        // unique ID to break ties
    int version;   // bump whenever we update val/cnt
    bool active;   // is this node still in the list?
    Node *prev, *next;
};

struct Entry {
    Node *p;
    int ver;       // version of p when this entry was pushed
};

// Min‐heap comparator: smallest val, then smallest id
struct Cmp {
    bool operator()(Entry const &A, Entry const &B) const {
        if (A.p->val != B.p->val)
            return A.p->val > B.p->val;
        return A.p->id > B.p->id;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector<int> A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }

        // Build the run‐list (value, count)
        vector<pair<int,int>> runs;
        runs.reserve(N);
        int curv = A[0], curc = 1;
        for (int i = 1; i < N; i++) {
            if (A[i] == curv) {
                curc++;
            } else {
                runs.emplace_back(curv, curc);
                curv = A[i];
                curc = 1;
            }
        }
        runs.emplace_back(curv, curc);

        int R = runs.size();
        // Create nodes
        vector<Node> nodes(R);
        for (int i = 0; i < R; i++) {
            nodes[i].val     = runs[i].first;
            nodes[i].cnt     = runs[i].second;
            nodes[i].id      = i;
            nodes[i].version = 0;
            nodes[i].active  = true;
            nodes[i].prev    = (i>0 ? &nodes[i-1] : nullptr);
            nodes[i].next    = (i+1<R ? &nodes[i+1] : nullptr);
        }

        // Min‐heap of Entries
        priority_queue<Entry, vector<Entry>, Cmp> pq;
        for (int i = 0; i < R; i++) {
            pq.push({ &nodes[i], 0 });
        }

        long long answer = 0;
        // We process until the single remaining node has cnt==1
        while (!pq.empty()) {
            Entry e = pq.top(); pq.pop();
            Node *u = e.p;
            // discard stale or already‐removed nodes
            if (!u->active || u->version != e.ver) 
                continue;

            // If it's the only node left AND count==1, we're done
            if (u->prev==nullptr && u->next==nullptr && u->cnt==1) {
                break;
            }

            // If count is odd, insert one more to make it even
            int ins = u->cnt & 1;
            answer += ins;
            int newVal   = u->val + 1;
            int newCount = (u->cnt + ins) / 2;

            // Bump version to invalidate old heap entries
            u->version++;

            // Try to merge with left neighbor if it has the same newVal
            Node *L = u->prev;
            if (L && L->active && L->val == newVal) {
                newCount += L->cnt;
                L->active = false;
                Node *LL = L->prev;
                u->prev = LL;
                if (LL) LL->next = u;
            }

            // Try to merge with right neighbor similarly
            Node *Rr = u->next;
            if (Rr && Rr->active && Rr->val == newVal) {
                newCount += Rr->cnt;
                Rr->active = false;
                Node *RR = Rr->next;
                u->next = RR;
                if (RR) RR->prev = u;
            }

            // Update this node and re‐push
            u->val = newVal;
            u->cnt = newCount;
            pq.push({u, u->version});
        }

        cout << answer << "\n";
    }
    return 0;
}