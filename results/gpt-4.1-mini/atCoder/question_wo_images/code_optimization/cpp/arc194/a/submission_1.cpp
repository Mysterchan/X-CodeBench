#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    // We maintain a stack representing S.
    // For each element, we decide to append or delete last element to maximize sum.
    // If the current element is positive or zero, always append.
    // If negative, we can consider deleting last element if it improves sum.
    // But since we must perform exactly one operation per element,
    // and can delete only if stack not empty,
    // the optimal strategy is:
    // - If a[i] >= 0, append it.
    // - Else if stack not empty and top element > a[i], pop top (delete last element),
    //   else append a[i].
    // This greedy approach works because deleting last element removes a possibly large negative or smaller element,
    // making room for better sum.

    // However, the problem states we must perform exactly one operation per element:
    // append a[i] or delete last element (if not empty).
    // So for negative a[i], deleting last element is beneficial only if top element is less than a[i].
    // But since deleting removes top element, and we don't add a[i], we must check if deleting is better than appending a[i].

    // Actually, the problem allows any sequence of operations, so the best sum is the maximum sum of a subsequence
    // that can be formed by these operations, with the constraint that at each step we do exactly one operation:
    // append current element or delete last element (if not empty).

    // This is equivalent to finding the maximum sum of a subsequence where the order is preserved,
    // but we can delete previously appended elements by deleting last element(s).
    // The problem reduces to finding the maximum sum of a subsequence where we can remove elements from the end.

    // The optimal solution is to maintain a stack of elements representing S.
    // For each a[i]:
    // - If a[i] >= 0, append it.
    // - Else, if stack not empty and top element > a[i], delete top element (pop),
    //   else append a[i].

    // But we must perform exactly one operation per element.
    // So for negative a[i], if stack empty, must append a[i].
    // If stack not empty, compare top element and a[i]:
    // - If top element > a[i], delete top element (pop).
    // - Else append a[i].

    // This greedy approach ensures maximum sum.

    vector<ll> stack;
    ll sum = 0;
    for (int i = 0; i < n; ++i) {
        if (a[i] >= 0) {
            stack.push_back(a[i]);
            sum += a[i];
        } else {
            if (!stack.empty() && stack.back() > a[i]) {
                sum -= stack.back();
                stack.pop_back();
            } else {
                stack.push_back(a[i]);
                sum += a[i];
            }
        }
    }

    cout << sum << "\n";
    return 0;
}