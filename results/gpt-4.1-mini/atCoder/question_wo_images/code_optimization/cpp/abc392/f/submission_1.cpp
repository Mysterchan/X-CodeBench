#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node *left, *right;
    int size;
    int priority;
    Node(int v) : val(v), left(nullptr), right(nullptr), size(1), priority(rand()) {}
};

int getSize(Node* t) {
    return t ? t->size : 0;
}

void update(Node* t) {
    if (t) {
        t->size = 1 + getSize(t->left) + getSize(t->right);
    }
}

void split(Node* t, int k, Node*& left, Node*& right) {
    if (!t) {
        left = right = nullptr;
        return;
    }
    int leftSize = getSize(t->left);
    if (k <= leftSize) {
        split(t->left, k, left, t->left);
        right = t;
    } else {
        split(t->right, k - leftSize - 1, t->right, right);
        left = t;
    }
    update(t);
}

Node* merge(Node* left, Node* right) {
    if (!left || !right) return left ? left : right;
    if (left->priority > right->priority) {
        left->right = merge(left->right, right);
        update(left);
        return left;
    } else {
        right->left = merge(left, right->left);
        update(right);
        return right;
    }
}

void inorder(Node* t, vector<int>& res) {
    if (!t) return;
    inorder(t->left, res);
    res.push_back(t->val);
    inorder(t->right, res);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    vector<int> P(n);
    for (int i = 0; i < n; i++) cin >> P[i];

    Node* root = nullptr;
    for (int i = 0; i < n; i++) {
        Node *left, *right;
        // Insert i+1 at position P[i]
        split(root, P[i] - 1, left, right);
        Node* newNode = new Node(i + 1);
        root = merge(merge(left, newNode), right);
    }

    vector<int> ans;
    ans.reserve(n);
    inorder(root, ans);
    for (int x : ans) cout << x << ' ';
    cout << '\n';

    return 0;
}