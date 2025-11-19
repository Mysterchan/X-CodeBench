import java.io.*;
import java.util.*;

class Main {
	static final int INF = Integer.MAX_VALUE / 4;
	int N, M, S, T;
	List<Integer>[] to;
	int[] ds, dt;
	int[] from, shortest;
	int ans, len;

	@SuppressWarnings("unchecked")
	void main() {
		int[] ns = nextInts();
		N = ns[0]; M = ns[1]; S = ns[2] - 1; T = ns[3] - 1;
		to = new List[N]; Arrays.setAll(to, i -> new ArrayList<>());
		for (int i = 0; i < M; i++) {
			int[] uv = nextInts();
			int u = uv[0] - 1, v = uv[1] - 1;
			to[u].add(v); to[v].add(u);
		}
		dt = new int[N]; Arrays.fill(dt, INF);

		calcDsandShortest();
		calcDt();

		ans = INF;
		ans = Math.min(ans, ansByDodging());
		ans = Math.min(ans, ansByGoingBack());
		ans = Math.min(ans, ansByTakingNextPath());

		System.out.println( (ans == INF)? -1 : ans);
	}

	void calcDsandShortest() {
		ds = new int[N]; Arrays.fill(ds, INF);
		from = new int[N];
		var q = new ArrayDeque<int[]>();
		q.addLast(new int[] { S, 0, S });
		while (!q.isEmpty()) {
			var p = q.pollFirst();
			int n = p[0], d = p[1], f = p[2];
			if (ds[n] != INF) continue;
			ds[n] = d; from[n] = f;
			for (int v: to[n])
				if (ds[v] == INF) q.addLast(new int[] { v, d+1, n });
		}
		var path = new ArrayList<Integer>();
		int p = T; path.add(p);
		while (p != S) {
			path.add(p = from[p]);
		}
		len = path.size();
		shortest = new int[len]; Arrays.setAll(shortest, i -> path.get(len - 1 - i));
	}

	void calcDt() {
		dt = new int[N]; Arrays.fill(dt, INF);
		var q = new ArrayDeque<int[]>();
		q.addLast(new int[] { T, 0 });
		while (!q.isEmpty()) {
			var p = q.pollFirst();
			int n = p[0], d = p[1];
			if (dt[n] != INF) continue;
			dt[n] = d;
			for (int v: to[n])
				if (dt[v] == INF) q.addLast(new int[] { v, d+1 });
		}
	}

	int ansByDodging() {
		int ans = INF;
		for (int i = 1; i < len-1; i++) {
			int p = shortest[i];
			for (int v: to[p]) {
				if (v == shortest[i-1] || v == shortest[i+1]) continue;
				ans = Math.min(ans, ds[p] + 1 + dt[v] + (len-1));
				ans = Math.min(ans, dt[p] + 1 + ds[v] + (len-1));
			}
		}
		return ans;
	}

	int ansByGoingBack() {
		int ans = INF, l = 0;
		int v = S, p = shortest[1];
		int b;
		while ((b = to[v].size()) == 2) {
			for (int n: to[v])
				if (n != p) { p = v; v = n; break; }
			if (v == S || v == T) break;
			l++;
		}
		if (b > 2)	ans = 2*(len - 1) + 4*l + 4;

		l = 0;
		v = T; p = shortest[len-2];
		while ((b = to[v].size()) == 2) {
			for (int n: to[v])
				if (n != p) { p = v; v = n; break; }
			if (v == S || v == T) break;
			l++;
		}
		if (b > 2)	ans = Math.min(ans, 2*(len - 1) + 4*l + 4);
		return ans;
	}

	int ansByTakingNextPath() {
		to[S].remove(Integer.valueOf(shortest[1]));
		int[] du = new int[N]; Arrays.fill(du, INF);
		var q = new ArrayDeque<int[]>();
		q.addLast(new int[] { S, 0 });
		while (!q.isEmpty()) {
			var p = q.pollFirst();
			int n = p[0], d = p[1];
			if (du[n] != INF) continue;
			if (n == T) return len-1 + d;
			if (ans < d) return INF;
			du[n] = d;
			for (int v: to[n])
				if (du[v] == INF) q.addLast(new int[] { v, d+1 });
		}
		return Math.min(INF, len-1 + du[T]);
	}

	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	String next() { try { return br.readLine(); } catch (Exception e) { return null; } }
	String[] nexts() { return next().split(" "); }

	static int i(String s) { return Integer.parseInt(s); }
	int nextInt() { return i(next()); }
	int[] nextInts() { return Arrays.stream(nexts()).mapToInt(Main::i).toArray(); }

	public static void main(String[] args) {
		new Main().main();
	}
}