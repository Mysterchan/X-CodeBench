import java.util.Scanner;
public class Main {

	public static void main(String args[]) {

		Scanner in = new Scanner(System.in);
		String s = in.nextLine();
		solv(s);
	}

	public static int solv(String s) {
		int ans = Integer.valueOf(s.substring(0,1)) * Integer.valueOf(s.substring(2,3));
		System.out.println(ans + "test");
		return ans;
	}

}