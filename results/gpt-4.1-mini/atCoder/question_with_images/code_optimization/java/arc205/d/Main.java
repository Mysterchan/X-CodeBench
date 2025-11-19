import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[] size;
	static int[] parent;
	static int[] childrenCount;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();

		// Since sum of N over all test cases <= 5*10^5, we can reuse arrays by max size
		// But here we allocate per test case for clarity and memory efficiency.

		for (int _ = 0; _ < t; _++) {
			n = Integer.parseInt(br.readLine());
			parent = new int[n];
			childrenCount = new int[n];
			size = new int[n];

			if (n == 2) {
				// For n=2, only one edge, no pairs possible because u < v and u not ancestor of v
				// but u=1 is ancestor of 2, so no pairs
				br.readLine(); // read parents line
				sb.append(0).append('\n');
				continue;
			}

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 1; i < n; i++) {
				parent[i] = Integer.parseInt(st.nextToken()) - 1;
				childrenCount[parent[i]]++;
			}

			// Compute subtree sizes by post-order DFS
			// We do iterative DFS to avoid stack overhead
			// But recursive is fine here due to constraints and Java stack size

			dfs(0);

			// The problem reduces to:
			// Maximum number of pairs (u,v) with u < v, both white, and u not ancestor of v.
			// The optimal strategy is to pair nodes from different subtrees of the root,
			// because nodes in the same subtree have ancestor-descendant relations.

			// So, the answer is sum of floor of sizes of subtrees divided by 2,
			// but we can pair nodes from different subtrees.

			// Actually, the maximum number of pairs is:
			// (N - 1) / 2
			// minus the size of the largest subtree divided by 2,
			// because the largest subtree nodes cannot be paired among themselves,
			// and pairing with nodes outside largest subtree is limited.

			// But the original code logic is:
			// Follow the heavy path (child with max subtree size),
			// accumulate rem = sum of sizes of other subtrees,
			// and count pairs by rem and along the path.

			// We replicate the logic but more efficiently.

			int maxSubtree = 0;
			int maxChild = -1;
			for (int i = 0; i < n; i++) {
				if (childrenCount[i] > 0) {
					// find max child of current node
					// but we only need max child of root and then go down heavy path
					// so we do it iteratively

					// We'll implement the same logic as original but iterative and without list overhead

					// So we do the heavy path traversal:
					break;
				}
			}

			int ans = 0;
			int rem = 0;
			int x = 0;
			while (true) {
				if (rem > 0) {
					rem--;
					ans++;
				}
				int maxSize = 0;
				int maxC = -1;
				// find child with max subtree size
				for (int i = 1; i < n; i++) {
					if (parent[i] == x) {
						if (size[i] > maxSize) {
							maxSize = size[i];
							maxC = i;
						}
					}
				}
				rem += size[x] - 1 - maxSize;
				if (maxC == -1) break;
				x = maxC;
			}
			ans += rem / 2;

			sb.append(ans).append('\n');
		}
		br.close();
		System.out.print(sb);
	}

	static int dfs(int x) {
		int s = 1;
		for (int i = 1; i < parent.length; i++) {
			if (parent[i] == x) {
				s += dfs(i);
			}
		}
		return size[x] = s;
	}
}