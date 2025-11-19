import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n=sc.nextInt();
            int px=sc.nextInt();
            int py=sc.nextInt();
            int qx=sc.nextInt();
            int qy=sc.nextInt();
            double []a=new double[n];
            double sum=0;
            double max=-1;
            for(int j=0;j<n;j++){
                a[j]=sc.nextDouble();
                if(a[j]>max)max=a[j];
                sum+=a[j];
            }

            double d= Math.pow((px-qx)*(px-qx)+(py-qy)*(py-qy),0.5);
            int z=0;
            max=Math.max(d,max);
            sum+=d;
            if (max>sum-max) {
                z=1;
            }
            if(z==1) System.out.println("no");
            else System.out.println("yes");

        }
        sc.close();
    }
}
