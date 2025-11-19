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
            int[] a=new int[n];
            for(int i=0;i<n;i++){
                a[i]=sc.nextInt();
            }
            int[] b=new int[m];
            for(int i=0;i<m;i++){
                b[i]=sc.nextInt();
            }
            // Count how many horizontal lasers are strictly between 0 and y
            // Since all a[i] satisfy 0 < a[i] < y, all n lasers count
            // Similarly for vertical lasers, all m lasers count
            // So minimum crossings = n + m
            System.out.println(n + m);
        }
    }
}