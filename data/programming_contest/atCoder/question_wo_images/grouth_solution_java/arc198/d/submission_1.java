import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.BitSet;
import java.util.NoSuchElementException;
import java.util.function.IntFunction;
import java.util.function.LongFunction;

public class Main {
	public static void main(String[] args) {
		Main o = new Main();
		o.solve();
	}

	ArrayList<Integer>[] edge = null;
	int[][] adj = null;
	int N = 0;
	public void solve() {
		FastScanner sc = new FastScanner(System.in);
		N = sc.nextInt();
		edge = new ArrayList[N];
		for (int i = 0; i < N; i++) {
			edge[i] = new ArrayList<>();
		}
		for (int i = 0; i < N - 1; i++) {
			int U = sc.nextInt() - 1;
			int V = sc.nextInt() - 1;
			edge[U].add(V);
			edge[V].add(U);
		}
		BitSet[] A = new BitSet[N];
		for (int i = 0; i < N; i++) {
			A[i] = new BitSet(N);
			String S = sc.next();
			for (int j = 0; j < N; j++) {
				if ( S.charAt(j) == '1' ) A[i].set(j);
			}
		}

		adj = new int[N][N];
		rec(0, -1);

		BitSet[] check = new BitSet[N];
		for (int i = 0; i < N; i++) {
			check[i] = new BitSet(N);
		}

		UnionFind uf = new UnionFind(N);
		for (int i = 0; i < N; i++) {
			for (int j = A[i].nextSetBit(i + 1); j >= 0; j = A[i].nextSetBit(j + 1)) {
				solve0(i, j, uf, check);
			}
		}
		int ans = N;

		BitSet[] used = new BitSet[N];
		BitSet[] palindrome = new BitSet[N];
		for (int i = 0; i < N; i++) {
			used[i] = new BitSet(N);
			palindrome[i] = new BitSet(N);
		}
		ArrayDeque<int[]> queue = new ArrayDeque<>();
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			queue.add(new int[] {i, i});
			used[i].set(i);
			palindrome[i].set(i);

		}
		while (true) {
			ArrayDeque<int[]> nqueue = new ArrayDeque<>();
			while (queue.size() > 0) {
				int[] p = queue.pollFirst();
				int i = p[0];
				int j = p[1];

				boolean ok = false;
				if ( uf.isSame(i, j) ) {
					if ( i == j ) {
						ok = true;
					} else {
						int ni = adj[i][j];
						int nj = adj[j][i];
						if ( ni == j || palindrome[ni].get(nj) ) {
							ok = true;
						}
					}
				}
				if ( ok ) {
					cnt += i == j ? 1 : 2;
					palindrome[i].set(j);
					palindrome[j].set(i);
				}

				if ( i == j ) {
					for (int n: edge[i]) {
						if ( used[j].get(n) ) continue;
						nqueue.add(new int[] {j, n});
						used[j].set(n);
						used[n].set(j);
					}
				} else {
					for (int k = 0; k <= 1; k++) {
						int a = p[k];
						int b = p[1 - k];
						for (int n: edge[a]) {
							if ( used[b].get(n) || n == adj[a][b] ) continue;
							nqueue.add(new int[] {b, n});
							used[b].set(n);
							used[n].set(b);
						}
					}
				}
			}
			if ( nqueue.size() == 0 ) break;
			queue = nqueue;
		}

		System.out.println(cnt);
	}

	void solve0(int i0, int j0, UnionFind uf, BitSet[] check) {
		int i = i0;
		int j = j0;
		while ( !check[i].get(j) && i != j ) {
			check[i].set(j);
			check[j].set(i);
			uf.unite(i, j);
			int ni = adj[i][j];
			int nj = adj[j][i];
			if ( ni == j ) break;
			i = ni;
			j = nj;
		}
	}

	BitSet rec(int cur, int par) {
		BitSet ret = new BitSet(N);
		Arrays.fill(adj[cur], par);
		adj[cur][cur] = -1;
		for (int c: edge[cur]) {
			if ( c == par ) continue;
			BitSet cb = rec(c, cur);
			for (int i = cb.nextSetBit(0); i >= 0; i = cb.nextSetBit(i + 1)) {
				adj[cur][i] = c;
			}
			ret.or(cb);
		}
		ret.set(cur);
		return ret;
	}

	class UnionFind {
	int[] parent = null;
	int[] size = null;

	UnionFind(int N) {
		parent = new int[N];
		size = new int[N];
		for ( int i = 0 ; i < N ; i++ ) {
			parent[i] = i;
			size[i] = 1;
		}
	}

	int root(int i) {
		return parent[i] == i ? i : (parent[i] = root(parent[i]));
	}
	int size(int i) {
		return size[root(i)];
	}

	void unite(int i, int j) {
		int ri = root(i);
		int rj = root(j);
		if ( ri == rj ) {
			return;
		} else {
			if ( size[ri] < size[rj] ) {
				parent[ri] = rj;
				size[rj] += size[ri];
			} else {
				parent[rj] = ri;
				size[ri] += size[rj];
			}
		}
	}

	boolean isSame(int i, int j) {
		return root(i) == root(j);
	}
}
	static final char LF = '\n';
	static final char SPACE = ' ';
	static final String YES = "Yes";
	static final String NO = "No";
	void print(int[] array, char sep) {
		print(array, sep, n -> n, 0, array.length);
	}
	void print(int[] array, char sep, IntFunction<Integer> conv) {
		print(array, sep, conv, 0, array.length);
	}
	void print(int[] array, char sep, IntFunction<Integer> conv, int start, int end) {
		StringBuilder ans = new StringBuilder();
		for (int i = start; i < end; i++) {
			ans.append(conv.apply(array[i]));
			ans.append(sep);
		}
		ans.deleteCharAt(ans.length() - 1);
		System.out.println(ans.toString());
	}
	void print(long[] array, char sep) {
		print(array, sep, n -> n, 0, array.length);
	}
	void print(long[] array, char sep, LongFunction<Long> conv) {
		print(array, sep, conv, 0, array.length);
	}
	void print(long[] array, char sep, LongFunction<Long> conv, int start, int end) {
		StringBuilder ans = new StringBuilder();
		for (int i = start; i < end; i++) {
			ans.append(conv.apply(array[i]));
			ans.append(sep);
		}
		ans.deleteCharAt(ans.length() - 1);
		System.out.println(ans.toString());
	}
	void printYesNo(boolean yesno) {
		System.out.println(yesno ? YES : NO);
	}
	void printDouble(double val, int digit) {
		System.out.println(String.format("%." + digit + "f", val));
	}

	class FastScanner {
		private final InputStream in;
		private final byte[] buf = new byte[1024];
		private int ptr = 0;
		private int buflen = 0;
		FastScanner( InputStream source ) { this.in = source; }
		private boolean hasNextByte() {
			if ( ptr < buflen ) return true;
			else {
				ptr = 0;
				try { buflen = in.read(buf); } catch (IOException e) { e.printStackTrace(); }
				if ( buflen <= 0 ) return false;
			}
			return true;
		}
		private int readByte() { if ( hasNextByte() ) return buf[ptr++]; else return -1; }
		private boolean isPrintableChar( int c ) { return 33 <= c && c <= 126; }
		private boolean isNumeric( int c ) { return '0' <= c && c <= '9'; }
		private void skipToNextPrintableChar() { while ( hasNextByte() && !isPrintableChar(buf[ptr]) ) ptr++; }
		public boolean hasNext() { skipToNextPrintableChar(); return hasNextByte(); }
		public String next() {
			if ( !hasNext() ) throw new NoSuchElementException();
			StringBuilder ret = new StringBuilder();
			int b = readByte();
			while ( isPrintableChar(b) ) { ret.appendCodePoint(b); b = readByte(); }
			return ret.toString();
		}
		public long nextLong() {
			if ( !hasNext() ) throw new NoSuchElementException();
			long ret = 0;
			int b = readByte();
			boolean negative = false;
			if ( b == '-' ) { negative = true; if ( hasNextByte() ) b = readByte(); }
			if ( !isNumeric(b) ) throw new NumberFormatException();
			while ( true ) {
				if ( isNumeric(b) ) ret = ret * 10 + b - '0';
				else if ( b == -1 || !isPrintableChar(b) ) return negative ? -ret : ret;
				else throw new NumberFormatException();
				b = readByte();
			}
		}
		public int nextInt() { return (int)nextLong(); }
		public double nextDouble() { return Double.parseDouble(next()); }
		public int[] nextIntArray(int N) { return nextIntArray(N, 0); }
		public int[] nextIntArray(int N, int offset) {
			int[] ret = new int[N];
			for (int i = 0; i < N; i++) ret[i] = nextInt() - offset;
			return ret;
		}
		public long[] nextLongArray(int N) {
			long[] ret = new long[N];
			for (int i = 0; i < N; i++) ret[i] = nextLong();
			return ret;
		}
		public String[] nextStringArray(int N) {
			String[] ret = new String[N];
			for (int i = 0; i < N; i++) ret[i] = next();
			return ret;
		}
	}
}