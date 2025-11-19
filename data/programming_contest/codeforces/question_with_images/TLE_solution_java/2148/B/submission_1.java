import java.util.*;
public class Main {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int m=sc.nextInt();
            int x=sc.nextInt();
            int y=sc.nextInt();
            int a[]=new int[n];
            for(int i=0;i<n;i++){
              a[i]=sc.nextInt();
            }
            int b[]=new int[m];
            for(int i=0;i<m;i++){
                b[i]=sc.nextInt();
            }
            int count=0;
            for(int i=0;i<n;i++){
                for(int j=0;j<y;j++){
                     if(a[i]==j){
                        count++;
                     }
                }
            }
            int count2=0;
            for(int i=0;i<m;i++){
                for(int j=0;j<x;j++){
                     if(b[i]==j){
                        count2++;
                     }
                }
            }
            System.out.println(count+count2);
        }
    }
}
