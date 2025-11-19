import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc= new Scanner(System.in);
    int t = sc.nextInt();
    while (t-- > 0) {

      long n=sc.nextLong(),m=sc.nextLong(),a=sc.nextLong(), b=sc.nextLong();
      if(n-a+1<a)a=n-a+1;
      if(m-b+1<b)b=m-b+1;
      System.out.println(Math.min(1+ans(a)+ans(m),1+ans(n)+ans(b)));

    }

  }
  public static long ans(long n){
    long cnt=0;
    while(n>1){
      n=(n+1)/2;
      cnt++;
    }
    return cnt;
  }
}
