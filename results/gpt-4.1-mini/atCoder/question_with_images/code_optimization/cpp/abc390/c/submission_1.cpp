#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int h, w;
    std::cin >> h >> w;
    std::vector<std::string> grid(h);
    int min_row = h, max_row = -1, min_col = w, max_col = -1;

    for (int i = 0; i < h; i++) {
        std::cin >> grid[i];
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == '#') {
                if (i < min_row) min_row = i;
                if (i > max_row) max_row = i;
                if (j < min_col) min_col = j;
                if (j > max_col) max_col = j;
            }
        }
    }

    // Check if all cells inside the rectangle are not '.' (white)
    for (int i = min_row; i <= max_row; i++) {
        for (int j = min_col; j <= max_col; j++) {
            if (grid[i][j] == '.') {
                std::cout << "No\n";
                return 0;
            }
        }
    }

    std::cout << "Yes\n";
    return 0;
}