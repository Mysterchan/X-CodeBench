import java.util.*;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int q = sc.nextInt();

		if(n < 2 || n > Math.pow(10, 6) || q < 1 || q > 3 * Math.pow(10, 5)){
		  sc.close();
		  return;
		}

		int a = sc.nextInt();
		int b = sc.nextInt();
		List<Integer> points = new ArrayList<Integer>();

		points.add(a);
		points.add(b);

		System.out.println("Yes");

		for(int i = 2; i <= q; i++){
		  a = sc.nextInt();
		  b = sc.nextInt();

		  String str = judge(a, b, n, points);

		  if(str.equals("error")){
		    sc.close();
		    return;
		  }else{
		    System.out.println(str);

		    if(str.equals("Yes")){
		      points.add(a);
		      points.add(b);
		      Collections.sort(points);
		    }
		  }
		}

		sc.close();
		return;
	}

	public static String judge(int a, int b, int n, List<Integer> points){
	  for(int p = 0, len = points.size(); p <= len; p++){
	    int x, y;
	    if(p == 0){
	      x = 0;
	      y = points.get(p);
	    }else if(p == len){
	      x = points.get(p - 1);
	      y = n + 1;
	    }else{
	      x = points.get(p - 1);
	      y = points.get(p);
	    }

	    if(a == x || b == x || a < 1 || a > b || b > n){
	      return "error";
	    }

	    if(a > x && b < y){
	      return "Yes";
	    }
	  }
	  return "No";
	}
}