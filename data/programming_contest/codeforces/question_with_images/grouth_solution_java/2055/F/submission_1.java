import java.io.*;
import java.util.*;

public class Main extends PrintWriter {
	Main() { super(System.out); }
	static class Scanner {
		Scanner(InputStream in) { this.in = in; } InputStream in;
		byte[] bb = new byte[1 << 15]; int i, n;
		byte getc() {
			if (i == n) {
				i = n = 0;
				try { n = in.read(bb); } catch (IOException e) {}
			}
			return i < n ? bb[i++] : 0;
		}
		int nextInt() {
			byte c = 0; while (c <= ' ') c = getc();
			int a = 0; while (c > ' ') { a = a * 10 + c - '0'; c = getc(); }
			return a;
		}
	}
	Scanner sc = new Scanner(System.in);
	public static void main(String[] $) {
		Main o = new Main(); o.main(); o.flush();
	}

	boolean verticalSplit(int[] ll, int[] rr, int n) {
		int l = ll[0], r = rr[0];
		if ((r - l & 1) == 1)
			return false;
		for (int i = 1; i < n; i++) {
			if (rr[i] - ll[i] != r - l || ll[i] >= (l + r) / 2 || (ll[i] + rr[i]) / 2 <= l)
				return false;
			l = ll[i]; r = rr[i];
		}
		return true;
	}

	boolean slantedSplit(int[] ll, int[] rr, int n) {
		long al = 0, ar = 0;
		for (int i = 0; i < n; i++) {
			al += ll[i];
			ar += rr[i];
		}
		long a_ = (ar - al) / 2;

		int[] mm = new int[n];
out:
		for (int o = 1; o * 2 <= n; o++) {
			mm[o - 1] = rr[o - 1];

			al -= ll[n - o];
			ar -= rr[o - 1];

			if (a_ + (long) (rr[o] - rr[0]) * (n - o) != ar - al)
				continue;

			boolean md = false, rd = false;
			for (int i = o; i < n; i++) {
				mm[i] = rr[i] - (mm[i - o] - ll[i - o]);
				if (mm[i] >= rr[i] || (i + o < n ? ll[i] >= mm[i] : ll[i] != mm[i]))
					continue out;
				if (i > o) {
					if (rr[i] - rr[i - 1] != mm[i - o] - mm[i - o - 1])
						continue out;
					if (rr[i] < rr[i - 1])
						rd = true;
					else if (rr[i] > rr[i - 1] && rd)
						continue out;
					if (mm[i] > mm[i - 1])
						md = true;
					else if (mm[i] < mm[i - 1] && md)
						continue out;
					if (mm[i] >= rr[i - 1] || rr[i] <= mm[i - 1])
						continue out;
				}
			}
			return true;
		}
		return false;
	}

	void main() {
		for (int t = sc.nextInt(); t-- > 0; ) {
			int n = sc.nextInt();
			int[] ll = new int[n];
			int[] rr = new int[n];
			for (int i = 0; i < n; i++) {
				ll[i] = sc.nextInt();
				rr[i] = sc.nextInt() + 1;
			}
			if (verticalSplit(ll, rr, n)) {
				println("YES");
				continue;
			}
			if (slantedSplit(ll, rr, n)) {
				println("YES");
				continue;
			}
			for (int i = 0; i < n; i++) {
				int tmp = ll[i]; ll[i] = -rr[i]; rr[i] = -tmp;
			}
			if (slantedSplit(ll, rr, n)) {
				println("YES");
				continue;
			}
			println("NO");
		}
	}
}
