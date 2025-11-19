import java.io.*;
import java.util.*;

class Main {
	int N, M, Q;
	Set<Integer>[] to;
	UnionFind uf;
	int[] q;
	int[][] uv;

	@SuppressWarnings("unchecked")
	void main() {
		int[] ns = nextInts();
		N = ns[0]; M = ns[1];
		to = new Set[N]; Arrays.setAll(to, i -> new HashSet<>());
		uf = new UnionFind(N);
		uv = new int[M][];
		for (int i = 0; i < M; i++) {
			uv[i] = nextInts();
			int u = uv[i][0] - 1, v = uv[i][1] - 1;
			to[u].add(v); to[v].add(u);
		}
		Q = nextInt();
		q = nextInts();
		var sb = new StringBuilder();
		for (int i = 0; i < Q; i++) {
			int x = q[i] - 1;
			int u = uf.getRoot(uv[x][0] - 1), v = uf.getRoot(uv[x][1] - 1);
			if (u == v) {
				sb.append(M); sb.append('\n');
				continue;
			}
			if (to[u].remove(v)) { to[v].remove(u); M--; }
			int b = u, s = v;
			if (to[b].size() < to[s].size()) { int t = b; b = s; s = t; }
			for (int sv: to[s]) {
				to[sv].remove(s); to[sv].add(b);
				if (!to[b].add(sv)) {
					M--;
				}
				uf.connect(s, b);
			}
			sb.append(M); sb.append('\n');
		}
		print(sb);
	}

	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	String next() { try { return br.readLine(); } catch (Exception e) { return null; } }
	String[] nexts() { return next().split(" "); }

	static int i(String s) { return Integer.parseInt(s); }
	int nextInt() { return i(next()); }
	int[] nextInts() { return Arrays.stream(nexts()).mapToInt(Main::i).toArray(); }

	void print(Object o) {
		try { System.out.write(o.toString().getBytes()); System.out.flush(); }
		catch (Exception e) { }
	}

	public static void main(String[] args) {
		new Main().main();
	}
}

final class UnionFind {
	int[] size, parent, map, imap;

	UnionFind(int n) {
		size = new int[n]; parent = new int[n]; map = new int[n]; imap = new int[n];
		for (int i = 0; i < n; i++) {
			size[i] = 1; parent[i] = map[i] = imap[i] = i;
		}
	}

	boolean isConnected(int x, int y) {
		return getRootInt(imap[x]) == getRootInt(imap[y]);
	}

	boolean connect(int x, int y) {
		int ix = getRootInt(imap[x]), iy = getRootInt(imap[y]);
		if (ix == iy) return false;
		if (size[ix] > size[iy]) {
			parent[iy] = ix; size[ix] += size[iy];
			int t = map[iy]; map[iy] = map[ix]; map[ix] = t;
			t = imap[iy]; imap[iy] = imap[ix]; imap[ix] = t;
		}
		else { parent[ix] = iy; size[iy] += size[ix]; }
		return true;
	}

	int getRootInt(int x) {
		if (x != parent[x]) parent[x] = getRootInt(parent[x]);
		return parent[x];
	}

	int getRoot(int x) {
		return map[getRootInt(imap[x])];
	}

	int size(int x) { return size[getRootInt(imap[x])]; }
}