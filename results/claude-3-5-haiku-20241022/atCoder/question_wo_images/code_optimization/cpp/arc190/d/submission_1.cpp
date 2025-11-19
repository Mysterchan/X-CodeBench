#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

template<class T>
size_t HashCombine(const size_t seed, const T &v) {
    return seed ^ (std::hash<T>()(v) + 0x9e3779b9 + (seed << 6) + (seed >> 2));
}

struct pair_hash {
    template<class T>
    size_t operator()(const pair<T, T> &p) const {
        return HashCombine(hash<T>()(p.first), p.second);
    }
};

using ll = long long;
using VarMap = unordered_map<pair<ll, ll>, ll, pair_hash>;

template<typename T>
T mod_pow(T x, T n, const T &p) {
    T ret = 1;
    while (n > 0) {
        if (n & 1) (ret *= x) %= p;
        (x *= x) %= p;
        n >>= 1;
    }
    return ret;
}

pair<vector<vector<ll>>, vector<vector<VarMap>>> matrix_mul(
    const int n,
    const pair<vector<vector<ll>>, vector<vector<VarMap>>> &aaa,
    const pair<vector<vector<ll>>, vector<vector<VarMap>>> &bbb,
    const int c,
    const int p
) {
    vector result_const(n, vector<ll>(n, 0));
    vector result_var(n, vector<VarMap>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            ll elm_const = 0;
            VarMap elm_var;
            elm_var.reserve(32);
            
            for (int k = 0; k < n; ++k) {
                ll ac = aaa.first[i][k];
                ll bc = bbb.first[k][j];
                elm_const += ac * bc;
                
                if (!aaa.second[i][k].empty()) {
                    for (const auto &[xa_ea, a]: aaa.second[i][k]) {
                        auto key1 = make_pair(xa_ea.first, c - xa_ea.second);
                        auto itr = bbb.second[k][j].find(key1);
                        if (itr != bbb.second[k][j].end()) {
                            auto key_c = make_pair(xa_ea.first, c);
                            elm_var[key_c] += a * itr->second;
                        }
                        auto key2 = make_pair(xa_ea.first, c - xa_ea.second - 1);
                        itr = bbb.second[k][j].find(key2);
                        if (itr != bbb.second[k][j].end()) {
                            auto key_c1 = make_pair(xa_ea.first, c - 1);
                            elm_var[key_c1] += a * itr->second;
                        }
                    }
                }
            }
            
            result_const[i][j] = elm_const % p;
            for (auto &[key, val]: elm_var) {
                val %= p;
            }
            result_var[i][j] = move(elm_var);
        }
    }

    if (c <= 3 || ((c - 1) & (c - 2)) == 0) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int k = 0; k < n; ++k) {
                    ll ac = aaa.first[i][k];
                    if (ac > 0 && !bbb.second[k][j].empty()) {
                        for (const auto &[xb_eb, b]: bbb.second[k][j]) {
                            if (c - 1 <= xb_eb.second && xb_eb.second <= c) {
                                result_var[i][j][xb_eb] += ac * b;
                                result_var[i][j][xb_eb] %= p;
                            }
                        }
                    }
                    ll bc = bbb.first[k][j];
                    if (bc > 0 && !aaa.second[i][k].empty()) {
                        for (const auto &[xa_ea, a]: aaa.second[i][k]) {
                            if (c - 1 <= xa_ea.second && xa_ea.second <= c) {
                                result_var[i][j][xa_ea] += a * bc;
                                result_var[i][j][xa_ea] %= p;
                            }
                        }
                    }
                }
            }
        }
    }
    return {result_const, result_var};
}

vector<vector<ll>> solve(const ll n, const ll p, const vector<vector<ll>> &mat) {
    if (p == 2) {
        return vector(n, vector(n, n % 2));
    }

    vector mat_const(n, vector<ll>(n, 0));
    vector mat_var(n, vector<VarMap>(n));
    ll zero = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] == 0) {
                mat_var[i][j][{zero, 1}] = 1;
                ++zero;
            } else {
                mat_const[i][j] = mat[i][j];
            }
        }
    }

    vector result_const(n, vector<ll>(n, 0));
    vector result_var(n, vector<VarMap>(n));
    for (int i = 0; i < n; ++i) result_const[i][i] = 1;
    auto result = make_pair(result_const, result_var);
    auto matrix = make_pair(mat_const, mat_var);

    ll rc = 0;
    ll bit = 1;
    while (bit <= p) {
        if (p & bit) {
            result = matrix_mul(n, result, matrix, rc + bit, p);
            rc += bit;
        }
        matrix = matrix_mul(n, matrix, matrix, bit + bit, p);
        bit <<= 1;
    }

    vector ans(n, vector<ll>(n, 0));
    const ll const_mul = mod_pow(p - 1, zero, p);
    const ll var_mul = mod_pow(p - 1, zero - 1, p);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            ll tmp = result.first[i][j] * const_mul % p;
            for (const auto &[x_e, c]: result.second[i][j]) {
                if (x_e.second == p - 1) {
                    tmp = (tmp - c * var_mul) % p;
                }
            }
            ans[i][j] = (tmp + p) % p;
        }
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    ll n, p;
    cin >> n >> p;
    vector mat(n, vector<ll>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> mat[i][j];
        }
    }
    vector<vector<ll>> ans = solve(n, p, mat);
    for (const auto &row: ans) {
        for (size_t i = 0; i < row.size(); ++i) {
            if (i > 0) cout << " ";
            cout << row[i];
        }
        cout << "\n";
    }
    return 0;
}