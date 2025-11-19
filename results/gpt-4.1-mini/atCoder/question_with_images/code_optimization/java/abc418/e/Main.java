import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)) {
			int n = sc.nextInt();
			int[] x = new int[n];
			int[] y = new int[n];
			for (int i = 0; i < n; i++) {
				x[i] = sc.nextInt();
				y[i] = sc.nextInt();
			}

			// Map to count pairs by normalized slope (dx, dy)
			Map<Long, Integer> slopeCount = new HashMap<>();
			// Map to count pairs by midpoint (sumX, sumY)
			Map<Long, Integer> midpointCount = new HashMap<>();

			for (int i = 0; i < n - 1; i++) {
				int xi = x[i], yi = y[i];
				for (int j = i + 1; j < n; j++) {
					int xj = x[j], yj = y[j];

					// Calculate slope vector (dx, dy) normalized
					int dx = xj - xi;
					int dy = yj - yi;

					// Normalize slope vector to avoid sign ambiguity
					if (dx == 0) {
						dy = 1;
					} else if (dy == 0) {
						dx = 1;
					} else {
						if (dx < 0) {
							dx = -dx;
							dy = -dy;
						}
						int g = gcd(Math.abs(dx), Math.abs(dy));
						dx /= g;
						dy /= g;
					}

					// Encode slope as a long key: upper 32 bits dx, lower 32 bits dy
					long slopeKey = (((long) dx) << 32) | (dy & 0xffffffffL);
					slopeCount.merge(slopeKey, 1, Integer::sum);

					// Midpoint sums (sumX, sumY)
					// Use long key: upper 32 bits sumX, lower 32 bits sumY
					long midKey = (((long) (xi + xj)) << 32) | ((yi + yj) & 0xffffffffL);
					midpointCount.merge(midKey, 1, Integer::sum);
				}
			}

			long ans = 0;
			for (int count : slopeCount.values()) {
				ans += (long) count * (count - 1) / 2;
			}

			long cnt = 0;
			for (int count : midpointCount.values()) {
				cnt += (long) count * (count - 1) / 2;
			}

			// Subtract pairs that form parallelograms (counted twice)
			ans -= cnt;

			System.out.println(ans);
		}
	}

	static int gcd(int a, int b) {
		while (b != 0) {
			int t = b;
			b = a % b;
			a = t;
		}
		return a;
	}
}