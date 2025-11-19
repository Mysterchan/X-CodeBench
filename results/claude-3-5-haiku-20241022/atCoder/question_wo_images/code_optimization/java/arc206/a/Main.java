import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		
		for(int i = 0;i < n;i++) {
			a[i] = sc.nextInt();
		}
		
		// Count positions for each value
		int[] count = new int[n + 1];
		for(int i = 0;i < n;i++) {
			count[a[i]]++;
		}
		
		// Store positions efficiently
		int[][] positions = new int[n + 1][];
		int[] idx = new int[n + 1];
		
		for(int i = 1;i <= n;i++) {
			positions[i] = new int[count[i] + 1];
			positions[i][count[i]] = n;
		}
		
		for(int i = 0;i < n;i++) {
			positions[a[i]][idx[a[i]]++] = i;
		}
		
		long ans = 1;
		
		for(int i = 1;i <= n;i++) {
			int size = positions[i].length;
			int[] pos = positions[i];
			
			for(int j = 0;j < size - 1;j++) {
				int curr = pos[j];
				int next = pos[j + 1];
				
				if(next == curr + 1) continue;
				
				ans += (n - curr - size + j + 1);
			}
		}
		
		System.out.print(ans);
	}

}