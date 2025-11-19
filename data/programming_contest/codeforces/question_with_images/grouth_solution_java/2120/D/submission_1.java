import java.util.*;

public class Main {
   static long  mod=1000000007;
    public static void main(String[] args) {
     Scanner sc=new Scanner(System.in);
     int t=sc.nextInt();
     long inv[]=new long[100001];
     inv[1]=1;
     for(int i=2;i<=100000;i++){
       inv[i]=(mod -mod/i)*inv[(int)mod%i]%mod;
     }
     while(t-->0){
       long a=sc.nextInt();
       long b=sc.nextInt();
       long k=sc.nextInt();
       long d=k*a-k+1;
       long ans=k;
       for(int i=1;i<=a;i++){
         ans=ans*((d-i+1)%mod)%mod*inv[i]%mod;

       }
       System.out.println(d%mod+ " "+ (ans*b-ans+1+mod)%mod);
     }
  }
}
