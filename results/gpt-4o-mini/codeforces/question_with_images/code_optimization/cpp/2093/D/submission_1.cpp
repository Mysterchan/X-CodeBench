#include <iostream>
using namespace std;

long long getValue(int n, int x, int y) {
    if (n == 1) {
        // Base case for 2x2 table
        if (x == 1 && y == 1) return 1;
        if (x == 1 && y == 2) return 4;
        if (x == 2 && y == 1) return 3;
        return 2; // (x == 2, y == 2)
    }
    
    int half = 1 << (n - 1); // half size of current table
    if (x <= half && y <= half) { // top-left
        return getValue(n - 1, x, y);
    } else if (x <= half && y > half) { // top-right
        return getValue(n - 1, x, y - half) + half * half;
    } else if (x > half && y <= half) { // bottom-left
        return getValue(n - 1, x - half, y) + 2 * half * half;
    } else { // bottom-right
        return getValue(n - 1, x - half, y - half) + 3 * half * half;
    }
}

void getCoordinates(int n, long long d, int& x, int& y) {
    long long totalCells = 1LL << (2 * n); // total cells in the table
    if (d < 1 || d > totalCells) return; // out of bounds
    d--; // Shift to 0-index
    
    for (int i = 0; i < n; i++) {
        long long size = 1LL << (2 * (n - i - 1)); // size of current divided table
        if (d < size) {
            // top-left quadrant
            x = (x == 0 ? 1 : x);
            y = (y == 0 ? 1 : y);
        } else if (d < 2 * size) {
            // top-right quadrant
            d -= size;
            y += size;
        } else if (d < 3 * size) {
            // bottom-left quadrant
            d -= 2 * size;
            x += size;
        } else {
            // bottom-right quadrant
            d -= 3 * size;
            x += size;
            y += size;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;

    while (t--) {
        int n, q;
        cin >> n >> q;
        
        while (q--) {
            string query;
            cin >> query;

            if (query[0] == '-') { // <- d
                long long d;
                cin >> d;
                int x = 0, y = 0;
                getCoordinates(n, d, x, y);
                cout << x << " " << y << "\n";
            } else { // -> x y
                int x, y;
                cin >> x >> y;
                long long value = getValue(n, x, y);
                cout << value << "\n";
            }
        }
    }

    return 0;
}