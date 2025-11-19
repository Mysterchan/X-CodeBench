import java.util.*;
public class Main {
	static long gcd(long a, long b) {
		while (b != 0) {
			long temp = b;
			b = a % b;
			a = temp;
		}
		return a;
	}
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long a[] = new long[n];
		for(int i=0;i<n;i++)
			a[i] = sc.nextLong();
		String ans = "Yes";
		if(n > 2) {
			long g = gcd(a[0], a[1]);
			long num = a[1] / g;
			long den = a[0] / g;
			for(int i=2;i<n;i++) {
				long g2 = gcd(a[i-1], a[i]);
				long num1 = a[i] / g2;
				long den1 = a[i-1] / g2;
				if(num * den1 != num1 * den) {
					ans = "No";
					break;
				}
			}
		}
		System.out.println(ans);
		sc.close();
	}
}