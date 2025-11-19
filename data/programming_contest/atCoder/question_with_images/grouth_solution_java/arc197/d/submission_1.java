import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Main {
	static List<Integer> sizeList;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int mod = 998244353;
		long[] f = new long[401];
		f[0] = 1;
		for (int i = 1; i < f.length; i++) {
			f[i] = f[i - 1] * i % mod;
		}
		f[0] = 0;
		PrintWriter pw = new PrintWriter(System.out);
		for (int z = 0; z < t; z++) {
			int n = Integer.parseInt(br.readLine());
			int[][] a = new int[n][n];
			for (int i = 0; i < n; i++) {
				String[] sa = br.readLine().split(" ");
				for (int j = 0; j < n; j++) {
					a[i][j] = Integer.parseInt(sa[j]);
				}
			}

			int cnt = 0;
			for (int i = 0; i < n; i++) {
				if (a[0][i] == 1) {
					cnt++;
				}
			}
			if (cnt != n) {
				pw.println(0);
				continue;
			}

			Map<Integer, Set<Integer>> map = new HashMap<>();
			for (int i = 1; i < n; i++) {
				Set<Integer> set = new HashSet<>();
				for (int j = 1; j < n; j++) {
					if (a[i][j] == 1) {
						set.add(j);
					}
				}
				map.put(i, set);
			}

			sizeList = new ArrayList<>();
			dfs(map);
			long ans = 1;
			for (int i : sizeList) {
				ans *= f[i];
				ans %= mod;
			}
			pw.println(ans);
		}
		pw.flush();
		br.close();
	}

	static void dfs(Map<Integer, Set<Integer>> map) {
		Integer k0 = map.keySet().iterator().next();
		Set<Integer> set1 = map.get(k0);
		List<Integer> all = new ArrayList<>();
		for (Integer e : set1) {
			boolean flg = true;
			for (Set<Integer> set : map.values()) {
				if (!set.contains(e)) {
					flg = false;
					break;
				}
			}
			if (flg) {
				all.add(e);
			}
		}
		if (!all.isEmpty()) {
			sizeList.add(all.size());
			for (Set<Integer> set : map.values()) {
				set.removeAll(all);
			}
			for (Integer k : all) {
				map.remove(k);
			}
		}

		if (map.isEmpty()) {
			return;
		}

		DSU uf = new DSU(map.size());
		Map<Integer, Integer> ki = new HashMap<>();
		int[] ik = new int[map.size()];
		int idx = 0;
		for (Integer k : map.keySet()) {
			if (map.get(k).isEmpty()) {
				throw new RuntimeException();
			}
			ki.put(k, idx);
			ik[idx] = k;
			idx++;
		}
		for (Integer k : map.keySet()) {
			Set<Integer> set2 = map.get(k);
			for (Integer e : set2) {
				uf.merge(ki.get(k), ki.get(e));
			}
		}
		if (all.isEmpty() && uf.num() == 1) {
			sizeList.add(0);
			return;
		}

		List<List<Integer>> grps = uf.groups();
		for (List<Integer> grp : grps) {
			Map<Integer, Set<Integer>> map2 = new HashMap<>();
			for (int e : grp) {
				int e2 = ik[e];
				map2.put(e2, map.get(e2));
			}
			dfs(map2);
		}
	}
}

class DSU {
	private int n;
	private int[] parentOrSize;
	private int num;

	public DSU(int n) {
		this.n = n;
		this.parentOrSize = new int[n];
		Arrays.fill(parentOrSize, -1);
		num = n;
	}

	int merge(int a, int b) {
		assert 0 <= a && a < n : "a=" + a;
		assert 0 <= b && b < n : "b=" + b;

		int x = leader(a);
		int y = leader(b);
		if (x == y) {
			return x;
		}
		if (-parentOrSize[x] < -parentOrSize[y]) {
			int tmp = x;
			x = y;
			y = tmp;
		}
		parentOrSize[x] += parentOrSize[y];
		parentOrSize[y] = x;
		num--;
		return x;
	}

	boolean same(int a, int b) {
		assert 0 <= a && a < n : "a=" + a;
		assert 0 <= b && b < n : "b=" + b;

		return leader(a) == leader(b);
	}

	int leader(int a) {
		assert 0 <= a && a < n : "a=" + a;

		if (parentOrSize[a] < 0) {
			return a;
		} else {
			return parentOrSize[a] = leader(parentOrSize[a]);
		}
	}

	int size(int a) {
		assert 0 <= a && a < n : "a=" + a;

		return -parentOrSize[leader(a)];
	}

	int num() {
		return num;
	}

	List<List<Integer>> groups() {
		int[] leaderBuf = new int[n];
		int[] groupSize = new int[n];
		for (int i = 0; i < n; i++) {
			leaderBuf[i] = leader(i);
			groupSize[leaderBuf[i]]++;
		}
		List<List<Integer>> result = new ArrayList<>(n);
		for (int i = 0; i < n; i++) {
			result.add(new ArrayList<>(groupSize[i]));
		}
		for (int i = 0; i < n; i++) {
			result.get(leaderBuf[i]).add(i);
		}
		result.removeIf(List::isEmpty);
		return result;
	}
}