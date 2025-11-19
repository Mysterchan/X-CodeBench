import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int t=sc.nextInt();
        List<Integer> ls;
        while(t>0){
            ls=new ArrayList<>();
            int n=sc.nextInt();
            int k=sc.nextInt();
            for(int i=n;i<2*n;i++){
                if((i^n)==(i-n)){
                    ls.add(i);
                }
                if(ls.size()==k){
                    System.out.println(ls.get(ls.size()-1));
                    break;
                }
            }
            if(ls.size()<k){
                System.out.println(-1);
            }
            t--;
        }
    }
}