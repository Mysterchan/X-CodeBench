import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		var t = sc.nextInt();
		var n = new int[t];
		var a = new int[t][];
		for (var i = 0; i < t; i++) {
			n[i] = sc.nextInt();
			a[i] = new int[n[i] * n[i]];
			for (var j = 0; j < a[i].length; j++) {
				a[i][j] = sc.nextInt();
			}
		}
		sc.close();

		var sb = new StringBuilder();
		for (var i = 0; i < t; i++) {
			var result = calc(n[i], a[i]);
			sb.append(result);
			sb.append("\r\n");
		}
		System.out.println(sb.toString());
	}

	private static int calc(int n, int[] a) {
		var sets = new ArrayList<HashSet<Integer>>();
		for (var i = 0; i < n; i++) {
			sets.add(new HashSet<Integer>());
		}
		for (var i = 0; i < n; i++) {
			for (var j = i; j < n; j++) {
				if (a[i * n + j] == 1) {
					sets.get(i).add(j);
					sets.get(j).add(i);
				}
			}
		}
		if (sets.get(0).size() != n) {
			return 0;
		}

		for (var i = 0; i < n; i++) {
			sets.get(i).remove(0);
		}
		var set = new TreeSet<Integer>();
		for (var i = 1; i < n; i++) {
			set.add(i);
		}
		var result = count(set, sets);
		return result;
	}

	private static int count(TreeSet<Integer> set, ArrayList<HashSet<Integer>> sets) {

		if (set.size() == 1) {
			return 1;
		}

		var result = 1L;
		var root = 0;
		for (var p : new HashSet<Integer>(set)) {
			if (sets.get(p).size() == set.size()) {
				root++;
				set.remove(p);
				for (var q : set) {
					sets.get(q).remove(p);
				}
			}
		}
		if (root > 1) {
			for (var i = 1; i < root; i++) {
				result *= i + 1;
				result %= 998244353;
			}
		}

		while (!set.isEmpty()) {
			var set2 = new TreeSet<Integer>();
			var p = set.first();
			var dq = new ArrayDeque<Integer>();
			set.remove(p);
			set2.add(p);
			dq.add(p);
			while (!dq.isEmpty()) {
				var p1 = dq.poll();
				for (var p2 : sets.get(p1)) {
					if (set.contains(p2)) {
						set.remove(p2);
						set2.add(p2);
						dq.add(p2);
					}
				}
			}
			result *= count(set2, sets);
			result %= 998244353;
		}

		return (int) (result % 998244353);
	}
}