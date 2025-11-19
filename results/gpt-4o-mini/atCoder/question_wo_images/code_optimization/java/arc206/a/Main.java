import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] A = new int[n];
		for (int i = 0; i < n; i++) {
			A[i] = sc.nextInt();
		}

		long ans = 0;
		Set<Integer> uniqueElements = new HashSet<>();
		int lastIndex = -1;

		for (int i = 0; i < n; i++) {
			if (!uniqueElements.contains(A[i])) {
				uniqueElements.add(A[i]);

				// Count the number of valid (L, R) pairs
				// Note that lastIndex is used to determine the start of new ranges
				ans += (long) (i - lastIndex) * (n - i);
				lastIndex = i;
			}
		}

		System.out.print(ans);
	}
}