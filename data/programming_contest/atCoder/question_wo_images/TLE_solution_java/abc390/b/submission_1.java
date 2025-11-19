import java.util.*;
public class Main {
	static int gcd(int a, int b) {
        int i;
        if (a < b)
            i = a;
        else
            i = b;
        for (; i > 1; i--) {
        	if (a % i == 0 && b % i == 0)
                return i;
        }
        return 1;
    }
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a[] = new int [n];
		for(int i=0;i<n;i++)
			a[i] = sc.nextInt();
		String ans = "Yes";
		if(n > 2) {
			int x = gcd(a[0],a[1]);
			int num = a[1] / x;
			int den = a[0] / x;
			for(int i=1;i<n;i++) {
				int y = gcd(a[i], a[i-1]);
				int num1 = a[i] / y;
				int den1 = a[i-1] / y;
				if(num != num1 || den != den1)
					ans = "No";
			}
		}
		System.out.println(ans);
		sc.close();
	}
}