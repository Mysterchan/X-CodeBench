import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int[] A = new int[N];

		for(int i = 0;i < N;i++) {
			A[i] = scanner.nextInt();
		}
		long count = 0;

		Arrays.sort(A);

		for(int i = 0;i < N;i++) {
			int target = A[i] / 2;
			int idx = upperBound(A,target);
			count += idx;
		}
		System.out.println(count);

	}

	static int upperBound(int[] arr,int target) {
		int left = 0;
		int right = arr.length;
		while(left < right) {
			int mid = (left + right) / 2;
			if(arr[mid] <= target) {
				left = mid + 1;
			}else {
				right = mid;
			}
		}
		return left;
	}

}