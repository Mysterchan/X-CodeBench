import java.io.*;
import java.util.*;

class Main {
	int N, Q, ei, whole;
	List<int[]>[] to;
	int[] idx, w;
	int[][] esec;
	SegmentTree st;

	@SuppressWarnings("unchecked")
	void main() {
		N = nextInt();
		to = new List[N]; Arrays.setAll(to, i -> new ArrayList<>());
		esec = new int[N-1][2];
		for (int i = 0; i < N-1; i++) {
			int[] uv = nextInts();
			int u = uv[0] - 1, v = uv[1] - 1;
			to[u].add(new int[] { v, i });
			to[v].add(new int[] { u, i });
		}
		idx = new int[N];
		w = new int[N]; Arrays.fill(w, 1);
		whole = N;
		st = new SegmentTree(w);
		dfs(0, -1, -1);

		Q = nextInt();
		var sb = new StringBuilder();
		for (int i = 0; i < Q; i++) {
			int[] q = nextInts();
			int x = q[1] - 1;
			switch (q[0]) {
				case 1:
					w[x] += q[2]; whole += q[2];
					st.update(idx[x], w[x]);
					break;
				default:
					int sum = st.calculate(esec[x][0], esec[x][1] + 1);
					sb.append(Math.abs(whole - sum - sum));
					sb.append('\n');
			}
		}

		print(sb);
	}

	void dfs(int n, int ni, int p) {
		if (ni > -1) {
			idx[n] = ++ei;
			esec[ni][0] = ei;
		}
		for (int[] v: to[n]) {
			if (v[0] == p) continue;
			dfs(v[0], v[1], n);
		}
		if (ni > -1) esec[ni][1] = ei;
	}

	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	String next() { try { return br.readLine(); } catch (Exception e) { return null; } }
	String[] nexts() { return next().split(" "); }

	static int i(String s) { return Integer.parseInt(s); }
	int nextInt() { return i(next()); }
	int[] nextInts() { return Arrays.stream(nexts()).mapToInt(Main::i).toArray(); }

	static long l(String s) { return Long.parseLong(s); }
	long nextLong() { return l(next()); }
	long[] nextLongs() { return Arrays.stream(nexts()).mapToLong(Main::l).toArray(); }

	void print(Object o) {
		try { System.out.write(o.toString().getBytes()); System.out.flush(); }
		catch (Exception e) { }
	}

	public static void main(String[] args) {
		new Main().main();
	}
}

class SegmentTree {

	private int m;

	private int[] st;

	SegmentTree(int[] value) {
		init(value.length);
		construct(value);
	}

	private void init(int size) {
		m = (size == 1)? 1 : Integer.highestOneBit(size - 1) << 1;
		st = new int[2*m-1];
	}

	void construct(int[] elements) {
		int n = elements.length;
		for (int i = 0; i < n; i++)
			st[m-1+i] = elements[i];
		for (int i = m-2; i >= 0; i--)
			st[i] = st[i*2+1] + st[i*2+2];
	}

	void update(int index, int element) {
		int i = m-1+index;
		st[i] = element;
		while (i > 0) {
			i = (i-1) >>> 1;
			st[i] = st[i*2 + 1] + st[i*2 + 2];
		}
	}

	int calculate(int s, int eExclusive) {
		return calcImpl(s, eExclusive, 0, 0, m);
	}

	private int calcImpl(int s, int eExcl, int n, int l, int r) {
		if (r <= s || eExcl <= l) return 0;
		if (s <= l && r <= eExcl) return st[n];
		int i = (l>>>1)+(r>>>1);
		int cl = calcImpl(s, eExcl, 2*n + 1, l, i);
		int cr = calcImpl(s, eExcl, 2*n + 2, i, r);
		return cl + cr;
	}

}