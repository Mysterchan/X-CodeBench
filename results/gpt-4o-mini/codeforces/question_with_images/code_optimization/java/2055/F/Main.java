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

	boolean canPartition(int[] l, int[] r, int n) {
		int total = 0;
		for (int i = 0; i < n; i++) {
			total += (r[i] - l[i] + 1);
		}

		if (total % 2 != 0) return false; // Just an extra safety

		int half = total / 2;
		int current = 0;

		for (int i = 0; i < n; i++) {
			current += (r[i] - l[i] + 1);

			if (current == half) return true;

			if (current > half) break;
		}

		return false;
	}

	void main() {
		int t = sc.nextInt();
		StringBuilder result = new StringBuilder();

		while (t-- > 0) {
			int n = sc.nextInt();
			int[] l = new int[n];
			int[] r = new int[n];

			for (int i = 0; i < n; i++) {
				l[i] = sc.nextInt();
				r[i] = sc.nextInt();
			}

			if (canPartition(l, r, n)) {
				result.append("YES\n");
			} else {
				result.append("NO\n");
			}
		}
		print(result);
	}
}