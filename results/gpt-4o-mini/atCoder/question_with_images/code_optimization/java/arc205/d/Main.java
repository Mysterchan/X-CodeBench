import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
	static int[] size;
	static int[] childCount;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		while (t-- > 0) {
			int n = Integer.parseInt(br.readLine());
			size = new int[n + 1]; // size[i] represents the size of the subtree rooted at i
			childCount = new int[n + 1]; // tracks the number of children for each node
			ArrayList<ArrayList<Integer>> tree = new ArrayList<>();

			for (int i = 0; i <= n; i++) {
				tree.add(new ArrayList<>());
			}
			
			String[] p = br.readLine().split(" ");
			for (int i = 2; i <= n; i++) {
				int p_i = Integer.parseInt(p[i - 2]); // parent of node i
				tree.get(p_i).add(i);
			}

			// DFS to calculate subtree sizes and child counts
			dfs(1, tree);
			
			int maxPairs = 0;
			for (int i = 1; i <= n; i++) {
				if (childCount[i] > 0) {
					maxPairs += (size[i] - 1) / 2; // each node can be paired with its sibling
				}
			}
			
			sb.append(maxPairs).append('\n');
		}
		
		br.close();
		System.out.print(sb.toString());
	}

	static void dfs(int node, ArrayList<ArrayList<Integer>> tree) {
		size[node] = 1; // count the node itself
		for (int child : tree.get(node)) {
			dfs(child, tree);
			size[node] += size[child]; // add size of child subtree
			childCount[node]++; // count this child
		}
	}
}