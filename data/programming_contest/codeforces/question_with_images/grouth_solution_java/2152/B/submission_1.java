import java.util.*;

public class Main {
    public static void main(String[] args) {
      Scanner sc=new Scanner(System.in);
      int t=sc.nextInt();
      while(t-->0){
      long n=sc.nextLong();
      long a=sc.nextLong();
      long b=sc.nextLong();
      long x=sc.nextLong();
      long y=sc.nextLong();
      long ansx=(a<x?x:(a==x?0:n-x));
      long ansy=(b<y?y:(b==y?0:n-y));
      System.out.println(Math.max(ansy,ansx));
      }
  }
}
