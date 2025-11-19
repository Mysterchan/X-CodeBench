import java.util.*;
public class Main{

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        Map<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<m;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            int slope=(a+b)%n;
            map.put(slope,map.getOrDefault(slope,0)+1);

        }
        long totalpair=(long) (m*(m-1)/2);
        long nonIntersecting=0;
        for(long pair:map.values()){
            nonIntersecting+= pair*(pair-1)/2;

        }
        long ans=totalpair-nonIntersecting;
        System.out.println(ans);

    }
}