
#include <bits/stdc++.h>

#define all(a) a.begin(),a.end()
#define len(a) (int)(a.size())
#define mp make_pair
#define pb push_back
#define fi first
#define se second

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
template<class T>
using vec = vector<T>;

template<typename T>
bool umin(T &a, T b) {
    if (b < a) {
        a = b;
        return true;
    }
    return false;
}

template<typename T>
bool umax(T &a, T b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

#ifdef KoRoVa
#define DEBUG for (bool _FLAG = true; _FLAG; _FLAG = false)
#define LOG(...) print(#__VA_ARGS__" ::", __VA_ARGS__) << endl
template <class ...Ts> auto &print(Ts ...ts) { return ((cerr << ts << " "), ...); }
#else
#define DEBUG while (false)
#define LOG(...)
#endif

const int max_n = 15e5, sqr = 1300, inf = 1000111222;

void test_case() {
    int n;
    cin>>n;
    vector<bool> is(max_n, true);
    vector<int> num(1300, 1300);
    while(n --)
    {
        int a, b;
        cin>>a>>b;
        if(a < max_n && is[a - 1])
        {
            for(int j = a; j < max_n; j += a)
                if(is[j - 1])
                {
                    is[j - 1] = false;
                    num[j/1300]--;
                }
        }
        int ind = 0;
        for(; ind < 1300; ind++)
        {
            if(num[ind] < b)
                b -= num[ind];
            else
                break;
        }
        int in = ind * 1300;
        for(; in < max_n; in++)
        {
            b -= is[in];
            if(!b)
                break;
        }
        cout<<in + 1<<'\n';
    }
}

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t = 1;


    while (t--) test_case();

    return 0;
}

