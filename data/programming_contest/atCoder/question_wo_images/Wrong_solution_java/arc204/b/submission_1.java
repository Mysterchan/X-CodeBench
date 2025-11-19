import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] sa = br.readLine().split(" ");
		int n = Integer.parseInt(sa[0]);
		int k = Integer.parseInt(sa[1]);
		int nk = n * k;
		sa = br.readLine().split(" ");
		int[] p = new int[nk];
		int[] pi = new int[nk];
		for (int i = 0; i < nk; i++) {
			p[i] = Integer.parseInt(sa[i]) - 1;
			pi[p[i]] = i;
		}
		br.close();

		int ans = 0;
		boolean[] b = new boolean[nk];
		for (int i = 0; i < nk; i++) {
			if (b[i]) {
				continue;
			}
			Set<Integer> target = new HashSet<>();
			int x = p[i];
			target.add(x);
			b[x] = true;
			while (x != i) {
				x = p[x];
				target.add(x);
				b[x] = true;
			}

			List<List<Integer>> list = new ArrayList<>(n);
			for (int j = 0; j < n; j++) {
				list.add(new ArrayList<>());
			}
			for (int e : target) {
				int en = pi[e] % n;
				list.get(en).add(e);
			}

			int times = target.size() - 1;
			for (int z = 0; z < times; z++) {

				boolean flg = false;
				label:
				for (int j = 0; j < n; j++) {
					List<Integer> wk = list.get(j);
					for (int j2 = 0; j2 < wk.size(); j2++) {
						int e = wk.get(j2);
						if (e % n == j) {
							int ei = pi[e];
							int e2 = p[e];
							p[e] = e;
							pi[e] = e;
							p[ei] = e2;
							pi[e2] = ei;
							ans++;
							flg = true;
							wk.remove(j2);
							break label;
						}
					}
				}
				if (flg) {
					continue;
				}

				label:
				for (int j = 0; j < n; j++) {
					List<Integer> wk = list.get(j);
					for (int j2 = 0; j2 < wk.size(); j2++) {
						int e = wk.get(j2);
						int ei = pi[e];
						int e2 = p[e];
						if (e2 % n == j) {
							p[e] = e;
							pi[e] = e;
							p[ei] = e2;
							pi[e2] = ei;
							flg = true;
							List<Integer> wk2 = list.get(e % n);
							for (int j22 = 0; j22 < wk2.size(); j22++) {
								if (wk2.get(j22) == e2) {
									wk2.remove(j22);
									break;
								}
							}
							wk.set(j2, e2);
							break label;
						}
					}
				}
				if (flg) {
					continue;
				}

				for (int j = 0; j < n; j++) {
					List<Integer> wk = list.get(j);
					if (wk.isEmpty()) {
						continue;
					}
					int j2 = wk.size() - 1;
					int e = wk.get(j2);
					int ei = pi[e];
					int e2 = p[e];
					p[e] = e;
					pi[e] = e;
					p[ei] = e2;
					pi[e2] = ei;
					flg = true;
					List<Integer> wk2 = list.get(e % n);
					for (int j22 = 0; j22 < wk2.size(); j22++) {
						if (wk2.get(j22) == e2) {
							wk2.remove(j22);
							break;
						}
					}
					wk.set(j2, e2);
					break;
				}
			}
		}
		System.out.println(ans);
	}
}