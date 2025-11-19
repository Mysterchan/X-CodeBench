import java.util.*;
public class Main {
    public static void main(String[] args) {
       Scanner sc=new Scanner(System.in);
       int n=sc.nextInt();
       int s[]=new int[n];;
       int c[]=new int[n];

       for(int i=0;i<n;i++){
           s[i]=sc.nextInt();
       }

       for(int i=0;i<n;i++){
           c[i]=sc.nextInt();
       }

       HashMap<Integer,ArrayList<Integer>>h=new HashMap<>();

       for(int i=0;i<n;i++){
           h.putIfAbsent(c[i],new ArrayList<>());
           h.get(c[i]).add(s[i]);
       }
       int tc=0;
       for(int i:h.keySet()){
           if(h.get(i).size()==1){
               continue;
           }
           int l=getlis(h.get(i));
           int fixlen=h.get(i).size()-l;
           tc+=i*fixlen;
       }System.out.println(tc);
    }private static int getlis(ArrayList<Integer>arr){

        int dp[]=new int[arr.size()];
        Arrays.fill(dp,1);
        dp[0]=1;
        int max=1;
        for(int i=1;i<arr.size();i++){
            for(int j=0;j<i;j++){
                if(arr.get(i)>arr.get(j)){
                    dp[i]=Math.max(dp[j]+1,dp[i]);
                    max=Math.max(max,dp[i]);
                }
            }
        }return max;

    }
}