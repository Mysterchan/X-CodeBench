import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)) {
			int n = sc.nextInt();

			List<Edge> edges = new ArrayList<>();
			List<List<Integer>> g = new ArrayList<>();
			for(int i = 0; i < n; i++) g.add(new ArrayList<Integer>());

			SegTree<Integer> seg = new SegTree<>(n, (a, b) -> a + b, 0);
			for(int i = 0; i < n; i++) seg.set(i, 1);

			for(int i = 0; i < n - 1; i++) {
				int u = sc.nextInt();
				int v = sc.nextInt();
				u--;
				v--;

				edges.add(new Edge(u, v));
				g.get(u).add(v);
				g.get(v).add(u);
			}

			int[] l = new int[n];
			int[] r = new int[n];

			F f = (ff, v, p, idx) -> {
				l[v] = idx;

				for(int to : g.get(v)) {
					if(to == p) continue;
					idx = ff.dfs(ff, to, v, idx + 1);
				}

				r[v] = idx;
				return r[v] = idx;
			};

			f.dfs(f, 0, -1, 0);

			int sum = n;
			StringBuilder sb = new StringBuilder();
			int q = sc.nextInt();
			for(int qi = 0; qi< q; qi++) {
				int t = sc.nextInt();
				if(t == 1) {
					int x = sc.nextInt();
					int w = sc.nextInt();
					x--;
					int idx = l[x];
					int v = seg.prod(idx, idx + 1);
					seg.set(idx, v + w);
					sum += w;
				}

				if(t == 2) {
					int y = sc.nextInt();
					y--;

					Edge e = edges.get(y);

					int v = Math.max(l[e.u], l[e.v]);
					int d = seg.prod(l[v], r[v] + 1);

					sb.append(Math.abs(sum - 2 * d)).append("\n");

				}
			}

			System.out.print(sb.toString());
		}
	}

	interface F {
		int dfs(F f, int v, int p, int idx);
	}
}

class Edge {
	int u;
	int v;

	public Edge(int u, int v) {
		this.u = u;
		this.v = v;
	}
}

class SegTree<S> {

	final int MAX;

	final int N;
	final java.util.function.BinaryOperator<S> op;
	final S E;

	final S[] data;

	@SuppressWarnings("unchecked")
	public SegTree(int n, java.util.function.BinaryOperator<S> op, S e) {
		MAX = n;
		int k = 1;
		while (k < n) k <<= 1;
		N = k;
		E = e;
		this.op = op;
		data = (S[]) new Object[N << 1];
		java.util.Arrays.fill(data, E);
	}

	public SegTree(S[] dat, java.util.function.BinaryOperator<S> op, S e) {
		this(dat.length, op, e);
		build(dat);
	}

	private void build(S[] dat) {
		int l = dat.length;
		System.arraycopy(dat, 0, data, N, l);
		for (int i = N - 1; i > 0; i--) {
			data[i] = op.apply(data[i << 1 | 0], data[i << 1 | 1]);
		}
	}

	public void set(int p, S x) {
		exclusiveRangeCheck(p);
		data[p += N] = x;
		p >>= 1;
		while (p > 0) {
			data[p] = op.apply(data[p << 1 | 0], data[p << 1 | 1]);
			p >>= 1;
		}
	}

	public void set(int p, java.util.function.UnaryOperator<S> f) {
		exclusiveRangeCheck(p);
		data[p += N] = f.apply(data[p]);
		p >>= 1;
		while (p > 0) {
			data[p] = op.apply(data[p << 1 | 0], data[p << 1 | 1]);
			p >>= 1;
		}
	}

	public S get(int p) {
		exclusiveRangeCheck(p);
		return data[p + N];
	}

	public S prod(int l, int r) {
		if (l > r) { throw new IllegalArgumentException(String.format("Invalid range: [%d, %d)", l, r)); }
		inclusiveRangeCheck(l);
		inclusiveRangeCheck(r);
		S sumLeft = E;
		S sumRight = E;
		l += N;
		r += N;
		while (l < r) {
			if ((l & 1) == 1) sumLeft = op.apply(sumLeft, data[l++]);
			if ((r & 1) == 1) sumRight = op.apply(data[--r], sumRight);
			l >>= 1;
			r >>= 1;
		}
		return op.apply(sumLeft, sumRight);
	}

	public S allProd() {
		return data[1];
	}

	public int maxRight(int l, java.util.function.Predicate<S> f) {
		inclusiveRangeCheck(l);
		if (!f.test(E)) { throw new IllegalArgumentException("Identity element must satisfy the condition."); }
		if (l == MAX) return MAX;
		l += N;
		S sum = E;
		do {
			l >>= Integer.numberOfTrailingZeros(l);
			if (!f.test(op.apply(sum, data[l]))) {
				while (l < N) {
					l = l << 1;
					if (f.test(op.apply(sum, data[l]))) {
						sum = op.apply(sum, data[l]);
						l++;
					}
				}
				return l - N;
			}
			sum = op.apply(sum, data[l]);
			l++;
		} while ((l & -l) != l);
		return MAX;
	}

	public int minLeft(int r, java.util.function.Predicate<S> f) {
		inclusiveRangeCheck(r);
		if (!f.test(E)) { throw new IllegalArgumentException("Identity element must satisfy the condition."); }
		if (r == 0) return 0;
		r += N;
		S sum = E;
		do {
			r--;
			while (r > 1 && (r & 1) == 1) r >>= 1;
			if (!f.test(op.apply(data[r], sum))) {
				while (r < N) {
					r = r << 1 | 1;
					if (f.test(op.apply(data[r], sum))) {
						sum = op.apply(data[r], sum);
						r--;
					}
				}
				return r + 1 - N;
			}
			sum = op.apply(data[r], sum);
		} while ((r & -r) != r);
		return 0;
	}

	private void exclusiveRangeCheck(int p) {
		if (p < 0 || p >= MAX) {
			throw new IndexOutOfBoundsException(
					String.format("Index %d out of bounds for the range [%d, %d).", p, 0, MAX));
		}
	}

	private void inclusiveRangeCheck(int p) {
		if (p < 0 || p > MAX) {
			throw new IndexOutOfBoundsException(
					String.format("Index %d out of bounds for the range [%d, %d].", p, 0, MAX));
		}
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append('[');
		for (int i = 0;i < N;++ i) {
			if (i != 0) sb.append(", ");
			sb.append(data[i + N]);
		}
		sb.append(']');
		return sb.toString();
	}
}