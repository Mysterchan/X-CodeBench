#include <iostream>
#include <vector>
#include <limits>

int main() {
    int h, w;
    std::cin >> h >> w;
    
    std::vector<std::string> grid(h);
    int min_row = std::numeric_limits<int>::max(), max_row = -1;
    int min_col = std::numeric_limits<int>::max(), max_col = -1;
    
    for (int i = 0; i < h; ++i) {
        std::cin >> grid[i];
        for (int j = 0; j < w; ++j) {
            if (grid[i][j] == '#') {
                min_row = std::min(min_row, i);
                max_row = std::max(max_row, i);
                min_col = std::min(min_col, j);
                max_col = std::max(max_col, j);
            }
        }
    }
    
    for (int i = min_row; i <= max_row; ++i) {
        for (int j = min_col; j <= max_col; ++j) {
            if (grid[i][j] == '.') {
                std::cout << "No";
                return 0;
            }
        }
    }
    
    std::cout << "Yes";
    return 0;
}