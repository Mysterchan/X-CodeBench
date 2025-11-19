import java.util.Scanner;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		var t = sc.nextInt();
		var n = new int[t];
		var a = new int[t][];
		var b = new int[t][];
		for (var i = 0; i < t; i++) {
			n[i] = sc.nextInt();
			a[i] = new int[n[i]];
			b[i] = new int[n[i]];
			for (var j = 0; j < n[i]; j++) {
				a[i][j] = sc.nextInt();
				b[i][j] = sc.nextInt();
			}
		}
		sc.close();

		var sb = new StringBuilder();
		for (var i = 0; i < t; i++) {
			var v = calc(n[i], a[i], b[i]);
			for (var v1 : v) {
				sb.append(v1 + 1);
				sb.append(" ");
			}
			sb.append("\r\n");
		}
		System.out.println(sb.toString());
	}

	private static int[] calc(int n, int[] a, int[] b) {
		var v = new int[n];
		var set1 = new TreeSet<Integer>(IntStream.range(0, n).boxed().collect(Collectors.toSet()));
		while (!set1.isEmpty()) {
			var p = p(set1, a, b);

			set1.remove(p);
			v[p] = set1.size();
		}
		return v;
	}

	private static int p(TreeSet<Integer> set1, int[] a, int[] b) {
		for (var p1 : set1.descendingSet()) {
			var check = true;
			for (var p2 : set1) {
				if (p1 == p2) {
					continue;
				}

				if (a[p2] < a[p1] && b[p1] < b[p2]) {
					check = false;
					break;
				}
			}
			if (check) {
				return p1;
			}
		}
		return 0;
	}
}