import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	static int n, ans, rem;
	static List<List<Integer>> list;
	static int[] size;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int z = 0; z < t; z++) {
			n = Integer.parseInt(br.readLine());
			list = new ArrayList<>(n);
			for (int i = 0; i < n; i++) {
				list.add(new ArrayList<>());
			}
			String[] sa = br.readLine().split(" ");
			for (int i = 0; i < n - 1; i++) {
				int p = Integer.parseInt(sa[i]) - 1;
				list.get(p).add(i + 1);
			}

			size = new int[n];
			dfs(0);
			ans = 0;
			rem = 0;

			int x = 0;
			while (true) {
				if (rem > 0) {
					rem--;
					ans++;
				}
				int max = 0;
				int mc = -1;
				for (int c : list.get(x)) {
					if (size[c] > max) {
						max = size[c];
						mc = c;
					}
				}
				rem += size[x] - 1 - max;
				if (mc == -1) {
					break;
				}
				x = mc;
			}

			ans += rem / 2;
			sb.append(ans).append('\n');
		}
		br.close();
		System.out.print(sb.toString());
	}

	static int dfs(int x) {
		int ret = 1;
		for (int c : list.get(x)) {
			ret += dfs(c);
		}
		return size[x] = ret;
	}

	static void dfs2(int x) {
		if (rem > 0) {
			rem--;
			ans++;
		}
		int max = 0;
		int mc = -1;
		for (int c : list.get(x)) {
			if (size[c] > max) {
				max = size[c];
				mc = c;
			}
		}
		rem += size[x] - 1 - max;
		if (mc != -1) {
			dfs2(mc);
		}
	}
}