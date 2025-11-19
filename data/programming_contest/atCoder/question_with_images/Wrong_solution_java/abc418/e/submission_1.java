import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;
public class Main
{
    static Scanner sc=new Scanner(System.in);
    static BufferedReader rd=new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter wd=new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws Exception{
        String d[];
        int times=1;
        while(times-->0){
            int n=Integer.parseInt(rd.readLine());
            int a[][]=new int[n][2];
            for(int i=0;i<n;i++){
                d=rd.readLine().split(" ");
                a[i][0]=    Integer.parseInt(d[0]);
                a[i][1]=    Integer.parseInt(d[1]);
            }
            long t=0,p=0;
            HashMap<Double,Integer>s=new HashMap<>();
            HashMap<String,Integer>md=new HashMap<>();
            String st;
            double x,y,slope;
            for(int i=0;i<n;i++){
                for(int j=i+1;j<n;j++){
                    x=a[j][0]-a[i][0];
                    y=a[j][1]-a[i][1];
                    if(x==0){
                        slope=Integer.MAX_VALUE;
                    }
                    else{
                        slope=y/x;
                    }
                    int z=s.getOrDefault(slope,0);
                    t+=z;
                    s.put(slope,z+1);
                    x=((double)a[i][0]+a[j][0])/2;
                    y=((double)a[i][1]+a[j][1])/2;
                    st=x+"_"+y;
                    z=md.getOrDefault(st,0);
                    p+=z;
                    md.put(st,z+1);
                }
            }
            System.out.println(t-p);
        }
        wd.flush();
	}
}