import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.TreeMap;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] sa = br.readLine().split(" ");
		int[] a = new int[n + 2];
		for (int i = 0; i < n; i++) {
			a[i + 1] = Integer.parseInt(sa[i]);
		}
		a[0] = 1;
		a[n + 1] = 1;

		int q = Integer.parseInt(br.readLine());
		int[] x = new int[q];
		for (int i = 0; i < q; i++) {
			x[i] = Integer.parseInt(br.readLine());
		}
		br.close();

		TreeMap<Integer, Integer> map = new TreeMap<>();
		for (int i = 1; i <= n; i++) {
			int a1 = a[i - 1];
			int a2 = a[i];
			if (a2 == 0) {
				if (a1 == 0) {
					int l = map.lowerKey(i);
					map.put(l, i);
				} else {
					map.put(i, i);
				}
			}
		}

		int zz = 0;
		for (int k : map.keySet()) {
			int v = map.get(k);
			if (k < v) {
				zz++;
			}
		}

		PrintWriter pw = new PrintWriter(System.out);
		for (int i = 0; i < q; i++) {
			int xi = x[i];
			int al = a[xi - 1];
			int am = a[xi];
			int ar = a[xi + 1];
			if (am == 0) {
				if (al == 0) {
					if (ar == 0) {
						int k = map.lowerKey(xi);
						map.put(xi + 1, map.get(k));
						map.put(k, xi - 1);
						zz--;
						if (xi + 1 < map.get(xi + 1)) {
							zz++;
						}
						if (k < xi - 1) {
							zz++;
						}
					} else {
						int k = map.lowerKey(xi);
						map.put(k, xi - 1);
						if (k == xi - 1) {
							zz--;
						}
					}
				} else {
					if (ar == 0) {
						map.put(xi + 1, map.get(xi));
						map.remove(xi);
						if (xi + 1 == map.get(xi + 1)) {
							zz--;
						}
					} else {
						map.remove(xi);
					}
				}
			} else {
				if (al == 0) {
					if (ar == 0) {
						int k = map.lowerKey(xi);
						if (k < map.get(k)) {
							zz--;
						}
						if (xi + 1 < map.get(xi + 1)) {
							zz--;
						}
						zz++;
						map.put(k, map.get(xi + 1));
						map.remove(xi + 1);
					} else {
						int k = map.lowerKey(xi);
						if (k < map.get(k)) {
							zz--;
						}
						zz++;
						map.put(k, xi);
					}
				} else {
					if (ar == 0) {
						if (xi + 1 < map.get(xi + 1)) {
							zz--;
						}
						zz++;
						map.put(xi, map.get(xi + 1));
						map.remove(xi + 1);
					} else {
						map.put(xi, xi);
					}
				}
			}
			a[xi] = 1 - a[xi];

			if (zz == 0) {
				if (a[1] == 0 && a[n] == 0) {
					pw.println(3);
				} else {
					pw.println(2);
				}
			} else {
				int ans = zz * 2 + zz - 1;
				int k1 = map.firstKey();
				if (k1 == 1) {
					int v1 = map.get(k1);
					if (k1 == v1) {
						ans += 2;
					}
				} else {
					ans++;
				}
				int kn = map.lastKey();
				int vn = map.get(kn);
				if (vn == n) {
					if (kn == vn) {
						ans += 2;
					}
				} else {
					ans++;
				}
				pw.println(ans);
			}
		}
		pw.flush();
	}
}