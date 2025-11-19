import java.util.*;
public class Main{
 public static void main(String[] args){
  Scanner sc=new Scanner(System.in);
  int t=sc.nextInt();
  while(t-->0){
   int n=sc.nextInt();
   long px=sc.nextLong(), py=sc.nextLong();
   long qx=sc.nextLong(), qy=sc.nextLong();
   long sum=0, max=0;
   for(int i=0;i<n;i++){
    long v=sc.nextLong();
    sum+=v;
    if(v>max) max=v;
   }
   double dx=qx-px, dy=qy-py;
   double D=Math.hypot(dx,dy);
   double rest=sum-max;
   double L = max>rest ? max-rest : 0;
   double R = sum;
   System.out.println((L<=D && D<=R) ? "Yes":"No");
  }
  sc.close();
 }
}
