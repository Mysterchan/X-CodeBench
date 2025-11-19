#include <bits/stdc++.h>
using namespace std;

template <typename T> void set_min(T& a, const T& b){
	if(b < a) a = b;
}
template <typename T> void set_max(T& a, const T& b){
	if(b > a) a = b;
}

struct UF {
    int n;
    vector<int> par;
    UF(int _n) : n(_n) {
        for(int i = 0; i < n; i++) par.push_back(i);
    }
    int find(int a){
        if(a != par[a]) par[a] = find(par[a]);
        return par[a];
    }
    bool join(int a, int b){
        a = find(a);
        b = find(b);
        par[a] = b;
        return (a != b);
    }
};

using ll = int64_t;

struct vtx_dp {
	ll v[3];
};

struct edge_dp {
	ll v[3][3];
};

void solve(){
	int N, M;
	cin >> N >> M;
	vector<pair<int,int> > edges;
	for(int i = 0; i < M; i++){
		int u, v;
		cin >> u >> v;
		u--; v--;
		edges.push_back({u, v});
	}
	M = (int)edges.size();
	vtx_dp v_empty;
	edge_dp e_empty;
	for(int a = 0; a < 3; a++) v_empty.v[a] = 0;
	for(int a = 0; a < 3; a++) for(int b = 0; b < 3; b++) e_empty.v[a][b] = 0;
	auto merge_into = [&](vtx_dp v, edge_dp e, vtx_dp w) -> vtx_dp {
		vtx_dp ret = v_empty;
		for(int a = 0; a <= 2; a++){
			for(int b = 0; a+b <= 2; b++){
				for(int c = 0; c <= 2; c++){
					for(int d = 0; c+d <= 2; d++){
						set_max(ret.v[a+b], v.v[a] + e.v[b][c] + w.v[d]);
					}
				}
			}
		}
		return ret;
	};
	auto merge_series = [&](edge_dp e1, vtx_dp v, edge_dp e2) -> edge_dp {
		edge_dp ret = e_empty;
		for(int a = 0; a <= 2; a++){
			for(int b = 0; b <= 2; b++){
				for(int c = 0; b+c <= 2; c++){
					for(int d = 0; b+c+d <= 2; d++){
						for(int e = 0; e <= 2; e++){
							set_max(ret.v[a][e], e1.v[a][b] + v.v[c] + e2.v[d][e]);
						}
					}
				}
			}
		}
		return ret;
	};
	auto merge_parallel = [&](edge_dp e1, edge_dp e2) -> edge_dp {
		edge_dp ret = e_empty;
		for(int a = 0; a <= 2; a++){
			for(int b = 0; b <= 2; b++){
				for(int c = 0; a+c <= 2; c++){
					for(int d = 0; b+d <= 2; d++){
						set_max(ret.v[a+c][b+d], e1.v[a][b] + e2.v[c][d]);
					}
				}
			}
		}
		return ret;
	};
	vector<vector<int> > adj(N);
	vector<int> deg(N, 0);
	vector<vtx_dp> v_dp(N, v_empty);
	vector<edge_dp> e_dp(M, e_empty);
	map<pair<int,int>, int> edge_to_id;
	for(int i = 0; i < M; i++){
		e_dp[i].v[1][1] = 1;
		auto [x, y] = edges[i];
		deg[x]++;
		deg[y]++;
		edge_to_id[{x, y}] = i;
		edge_to_id[{y, x}] = i;
		adj[x].push_back(i);
		adj[y].push_back(i);
	}
	vector<int> vtx_alive(N, 1);
	vector<int> edge_alive(M, 1);
	vector<int> verts;
	for(int v = 0; v < N; v++) verts.push_back(v);
	auto get_eids = [&](int v) -> vector<int> {
		vector<int> eids;
		for(int eid : adj[v]){
			if(!edge_alive[eid]) continue;
			eids.push_back(eid);
		}
		return eids;
	};
	auto flip = [&](int eid) -> void {
		swap(edges[eid].first, edges[eid].second);
		edge_dp x = e_empty;
		for(int a = 0; a <= 2; a++){
			for(int b = 0; b <= 2; b++){
				x.v[b][a] = e_dp[eid].v[a][b];
			}
		}
		e_dp[eid] = x;
	};
	vector<int> deg0s;
	while(!verts.empty()){
		int v = verts.back();
		verts.pop_back();
		if(!vtx_alive[v]) continue;
		if(deg[v] == 0){
			deg0s.push_back(v);
		} else if(deg[v] == 1 || deg[v] == 2){
			vector<int> eids = get_eids(v);
			assert((int)eids.size() == deg[v]);
			if(deg[v] == 1){
				int eid = eids[0];
				if(edges[eid].second != v) flip(eid);
				assert(edges[eid].second == v);
				int w = edges[eid].first ^ edges[eid].second ^ v;
				v_dp[w] = merge_into(v_dp[w], e_dp[eid], v_dp[v]);

				deg[v]--;
				deg[w]--;
				vtx_alive[v] = 0;
				edge_alive[eid] = 0;
				verts.push_back(w);
				edge_to_id.erase({v, w});
				edge_to_id.erase({w, v});
			} else if(deg[v] == 2){
				int eid_0 = eids[0];
				int eid_1 = eids[1];
				if(edges[eid_0].second != v) flip(eid_0);
				assert(edges[eid_0].second == v);
				if(edges[eid_1].first != v) flip(eid_1);
				assert(edges[eid_1].first == v);

				int u = edges[eid_0].first;
				int w = edges[eid_1].second;
				deg[v] = 0;
				vtx_alive[v] = 0;
				edge_alive[eid_0] = edge_alive[eid_1] = 0;
				{
					edge_to_id.erase({u, v});
					edge_to_id.erase({w, v});
					edge_to_id.erase({v, w});
					edge_to_id.erase({v, u});
				}
				deg[u]--;
				deg[w]--;
				auto combined_dp = merge_series(e_dp[eid_0], v_dp[v], e_dp[eid_1]);
				if(edge_to_id.count({u, w})){
					int eid = edge_to_id[{u, w}];
					if(edges[eid].first != u) flip(eid);
					assert(edges[eid].first == u);
					assert(edges[eid].second == w);
					e_dp[eid] = merge_parallel(e_dp[eid], combined_dp);
					verts.push_back(u);
					verts.push_back(w);
				} else {
					int eid = M;
					M++;
					edges.push_back({u, w});
					edge_alive.push_back(1);
					e_dp.push_back(combined_dp);
					deg[u]++; deg[w]++;
					edge_to_id[{u, w}] = eid;
					edge_to_id[{w, u}] = eid;
					adj[u].push_back(eid);
					adj[w].push_back(eid);
				}
			}
		}
	}
	if(deg0s.empty()){
		assert(false);
	} else {
		auto dp = v_dp[deg0s.front()];
		ll ans = 0;
		for(int a = 0; a <= 2; a++){
			set_max(ans, dp.v[a]);
		}
		cout << ans << '\n';
	}
}

int main(){
	ios_base::sync_with_stdio(false), cin.tie(nullptr);	
	int T;
	cin >> T;
	while(T--) solve();
}
