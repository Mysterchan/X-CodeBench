import java.util.*;
public class Main{
  public static void main(String[] args){
      Scanner in=new Scanner(System.in);
      int t=in.nextInt();
      while(t-->0){
          int n=in.nextInt();
          int a=in.nextInt();
          int b=in.nextInt();
          System.out.println(((n-b)%2==0 && ((n-a)%2==0 || a<=b))?"YES":"NO");
      }
  }
}
