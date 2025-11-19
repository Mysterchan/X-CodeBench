import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		var n = sc.nextInt();
		var a = IntStream.range(0, n).mapToObj(x -> new Main().new Coordinate(sc.nextLong(), sc.nextLong()))
				.toArray(Coordinate[]::new);
		var b = IntStream.range(0, n).mapToObj(x -> new Main().new Coordinate(sc.nextLong(), sc.nextLong()))
				.toArray(Coordinate[]::new);
		sc.close();

		var distances = new ArrayList<Distance>();
		for (var i = 0; i < n; i++) {
			for (var j = 0; j < n; j++) {
				var dt = Math.sqrt(Math.pow(a[i].x - b[j].x, 2) + Math.pow(a[i].y - b[j].y, 2));
				distances.add(new Main().new Distance(i, j, dt));
			}
		}
		Collections.sort(distances);

		var bs = new Main().new BinSearch(n, distances);
		var result = bs.search();
		System.out.printf("%.12f\r\n", result);
	}

	public class BinSearch {
		private int n;
		private ArrayList<Distance> distances = new ArrayList<Distance>();
		private ArrayList<HashSet<Integer>> sets = new ArrayList<HashSet<Integer>>();

		public BinSearch(int n, ArrayList<Distance> distances) {
			this.n = n;
			this.distances = distances;
			for (var i = 0; i < n * 2 + 2; i++) {
				sets.add(new HashSet<Integer>());
			}
			for (var i = 0; i < n; i++) {
				sets.get(this.n * 2).add(i);
				sets.get(this.n + i).add(this.n * 2 + 1);
			}
		}

		public double search() {
			return search(0, this.distances.size() - 1);
		}

		public double search(int min, int max) {
			while (max - min > 1) {
				var mid = min + (max - min) / 2;
				if (check(mid)) {
					max = mid;
				} else {
					min = mid;
				}
			}
			if (check(min)) {
				max = min;
			}
			return this.distances.get(max).distance;
		}

		public boolean check(int index) {
			for (var i = 0; i < n; i++) {
				sets.get(i).clear();
			}
			for (var i = 0; i < index + 1; i++) {
				var distance = distances.get(i);
				sets.get(distance.p1).add(n + distance.p2);
			}
			var mf = new Main().new MaxFlow(this.n * 2 + 2, sets, this.n * 2, this.n * 2 + 1);
			var flow = mf.calc();
			var result = flow >= n;

			return result;
		}
	}

	public class Coordinate {
		private double x;
		private double y;

		public Coordinate(double x, double y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public boolean equals(Object obj) {
			if (!(obj instanceof Coordinate)) {
				return false;
			}
			var target = (Coordinate) obj;
			return target.x == this.x && target.y == y;
		}

		@Override
		public int hashCode() {
			return (int) (this.x + this.y);
		}
	}

	public class Distance implements Comparable<Distance> {
		private int p1;
		private int p2;
		private double distance;

		public Distance(int p1, int p2, double distance) {
			this.p1 = p1;
			this.p2 = p2;
			this.distance = distance;
		}

		@Override
		public int compareTo(Distance target) {
			if (this.distance - target.distance > 0) {
				return 1;
			} else if (this.distance - target.distance < 0) {
				return -1;
			}
			return 0;
		}
	}

	public class MaxFlow {
		public int start = 0;
		public int goal = 0;
		private int[][] graph;
		private ArrayList<HashSet<Integer>> sets;

		public MaxFlow(int n, ArrayList<HashSet<Integer>> sets, int start, int goal) {
			this.start = start;
			this.goal = goal;
			this.graph = new int[n][n];
			this.sets = new ArrayList<HashSet<Integer>>();
			for (var i = 0; i < sets.size(); i++) {
				this.sets.add(new HashSet<Integer>());
				for (var j : sets.get(i)) {
					this.sets.get(i).add(j);
					graph[i][j] = 1;
				}
			}
		}

		public long calc() {
			var maxFlow = 0L;
			var set = new HashSet<Integer>();
			var list = new ArrayList<Integer>();
			while (true) {
				set.clear();
				list.clear();
				var flow = search(sets, this.start, Long.MAX_VALUE, set, list);
				if (flow == 0L) {
					break;
				}
				maxFlow += flow;
				Collections.reverse(list);
				for (var i = 0; i < list.size() - 1; i++) {
					var p1 = list.get(i);
					var p2 = list.get(i + 1);
					graph[p1][p2] -= flow;
					graph[p2][p1] += flow;
					sets.get(p2).add(p1);
					if (graph[p1][p2] <= 0) {
						sets.get(p1).remove(p2);
					}
				}
			}
			return maxFlow;
		}

		public long search(ArrayList<HashSet<Integer>> sets, int p, long f, HashSet<Integer> set, List<Integer> list) {
			if (p == this.goal) {
				list.add(p);
				return f;
			}
			set.add(p);
			for (var p2 : sets.get(p)) {
				if (graph[p][p2] > 0 && !set.contains(p2)) {
					var f2 = Math.min(f, graph[p][p2]);
					var result = search(sets, p2, f2, set, list);
					if (result > 0) {
						list.add(p);
						return result;
					}
				}
			}
			return 0;
		}
	}
}