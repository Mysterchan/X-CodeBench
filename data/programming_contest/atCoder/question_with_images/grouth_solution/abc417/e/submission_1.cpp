#include <iostream>
#include <cassert>
#include <vector>
#include <functional>
#include <queue>
#include <algorithm>

static std::vector<int> solve(const std::vector<std::vector<int>> &adj_list, const int source, const int target) {
    int n_vex = static_cast<int>(adj_list.size());
    std::vector<std::vector<bool>> reachable_matrix(n_vex, std::vector<bool>(n_vex, false));
    for(int i = 0;i < n_vex;++i) {
        reachable_matrix[i][i] = true;
        std::queue<int> q;
        q.push(i);
        while (!q.empty()) {
            const auto u = q.front();
            q.pop();
            for(const auto &v : adj_list[u]) {
                if (reachable_matrix[i][v]) {
                    continue;
                }
                reachable_matrix[i][v] = true;
                q.push(v);
            }
        }
    }
    std::vector<int> result;
    std::vector<bool> marked(n_vex, false);
    std::function<bool(int)> dfs = [&](int current_vex)->bool {
        if (marked[current_vex]) {
            return false;
        }
        marked[current_vex] = true;
        result.emplace_back(current_vex);
        if (current_vex == target) {
            return true;
        }
        for(const auto &next_vex : adj_list[current_vex]) {
            if (!marked[next_vex] && reachable_matrix[target][next_vex]) {
                if (dfs(next_vex)) {
                    return true;
                }
            }
        }
        result.pop_back();
        return false;
    };
    if (dfs(source)) {
        return result;
    } else {
        return {};
    }
}

int main() {
    int T;
    std::cin >> T;
    for(int t = 0;t < T;++t) {
        int n_vex, n_edge, source, target;
        std::cin >> n_vex >> n_edge >> source >> target;
        assert(n_vex >= 0 && n_edge >= 0 && 1 <= source && source <= n_vex && 1 <= target && target <= n_vex);
        --source;
        --target;
        std::vector<std::vector<int>> adj_list(n_vex);
        for(int i = 0;i < n_edge;++i) {
            int u, v;
            std::cin >> u >> v;
            assert(1 <= u && u <= n_vex && 1 <= v && v <= n_vex);
            --u;
            --v;
            adj_list[u].emplace_back(v);
            adj_list[v].emplace_back(u);
        }
        for(int i = 0;i < n_vex;++i) {
            std::sort(adj_list[i].begin(), adj_list[i].end());
        }
        const auto result = solve(adj_list, source, target);
        for(size_t i = 0;i < result.size();++i) {
            std::cout << result[i] + 1;
            if (i + 1 < result.size()) {
                std::cout << " ";
            } else {
                std::cout << "\n";
            }
        }
    }
    return 0;
}