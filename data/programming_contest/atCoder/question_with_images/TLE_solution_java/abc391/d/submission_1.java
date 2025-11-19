import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int w=sc.nextInt();
        HashMap<Integer, Integer>[] colum=new HashMap[w+1];
        for(int i=1; i<=w; i++){
            colum[i]=new HashMap<>();
        }
        HashSet<Integer> exist=new HashSet<>();
        for(int i=1; i<=n; i++){
            int x=sc.nextInt();
            int y=sc.nextInt();
            colum[x].put(y,i);
            exist.add(i);
        }
        boolean flag=true;
        int lowRow=1;
        ArrayList<String> time=new ArrayList<>();
        StringBuilder sb=new StringBuilder();
        for(int i:exist){
            sb.append(Integer.toString(i));
        }
        time.add(sb.toString());
        while(flag){
            ArrayList<Integer> mostLowRows=new ArrayList<>();
            for(int i=1; i<=w; i++){
                if(colum[i].size()==0){
                    flag=false;
                    break;
                }
                ArrayList<Integer> arrayRow=new ArrayList<>(colum[i].keySet());
                Collections.sort(arrayRow);
                for(int j=0; j<arrayRow.size(); j++){
                    if(arrayRow.get(j)==lowRow){
                        mostLowRows.add(colum[i].get(arrayRow.get(j)));
                    }else if(!colum[i].containsKey(arrayRow.get(j)-1)){
                        colum[i].put(arrayRow.get(j)-1,  colum[i].get(arrayRow.get(j)));
                        colum[i].remove(arrayRow.get(j));
                    }
                }
            }
            if(mostLowRows.size()==w){
                for(int i=0; i<mostLowRows.size(); i++){
                    exist.remove(mostLowRows.get(i));
                    colum[i+1].remove(lowRow);
                }
                lowRow++;
            }
            sb.delete(0, sb.length());
            for(int i:exist){
                sb.append(Integer.toString(i));
            }
            time.add(sb.toString());
        }
        int q=sc.nextInt();
        for(int i=0; i<q; i++){
            int t=sc.nextInt();
            int a=sc.nextInt();
            if(t>time.size()-1){
                if(time.get(time.size()-1).contains(Integer.toString(a))){
                    System.out.println("Yes");
                }else{
                    System.out.println("No");
                }
            }else if(time.get(t).contains(Integer.toString(a))){
                System.out.println("Yes");
            }else{
                System.out.println("No");
            }
        }
    }
}